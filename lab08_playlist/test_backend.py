"""Contract checks. Run with: uv run python -m unittest -v"""

import json
import unittest

from fastapi.testclient import TestClient
from backend import create_app


class PlaylistTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(create_app())
        self.addCleanup(self.client.close)

    def test_initial_playlist_and_page(self):
        response = self.client.get("/songs")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            {"id": 1, "title": "Blue Monday", "artist": "New Order", "votes": 3},
            {"id": 2, "title": "Clocks", "artist": "Coldplay", "votes": 1},
            {"id": 3, "title": "Dancing Queen", "artist": "ABBA", "votes": 0},
        ])
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertIn('id="playlist"', page.text)

    def test_add_and_preserve_order(self):
        for song_id, title, artist in [(4, "  New song  ", " Singer "),
                                       (5, "أغنية <new>", "A & B")]:
            response = self.client.post("/songs", json={"title": title, "artist": artist})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json(), {
                "id": song_id, "title": title.strip(), "artist": artist.strip(), "votes": 0
            })
        self.assertEqual([s["id"] for s in self.client.get("/songs").json()], [1, 2, 3, 4, 5])

    def test_invalid_input_does_not_store_or_consume_id(self):
        invalid = [{}, {"title": "Song"}, {"artist": "Artist"},
                   {"title": "", "artist": "Artist"},
                   {"title": "Song", "artist": " \t "},
                   {"title": None, "artist": "Artist"},
                   {"title": 123, "artist": "Artist"},
                   {"title": "Song", "artist": []}, [], None]
        for body in invalid:
            with self.subTest(body=body):
                response = self.client.post("/songs", content=json.dumps(body),
                                            headers={"Content-Type": "application/json"})
                self.assertEqual(response.status_code, 400)
                self.assertEqual(response.json(), {"error": "Title and artist are required."})
                self.assertEqual(len(self.client.get("/songs").json()), 3)
        self.assertEqual(self.client.post("/songs", json={"title": "OK", "artist": "OK"}).json()["id"], 4)

    def test_malformed_json(self):
        response = self.client.post("/songs", content="{", headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Request body must be valid JSON."})
        self.assertEqual(len(self.client.get("/songs").json()), 3)

    def test_votes_and_missing_song(self):
        for expected in range(4, 9):
            response = self.client.post("/songs/1/vote")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["votes"], expected)
        before = self.client.get("/songs").json()
        response = self.client.post("/songs/99999/vote")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "There is no song 99999"})
        self.assertEqual(self.client.get("/songs").json(), before)
        self.assertEqual([s["id"] for s in before], [1, 2, 3])

    def test_fresh_apps_are_isolated(self):
        self.client.post("/songs", json={"title": "Only here", "artist": "Me"})
        self.client.post("/songs/1/vote")
        with TestClient(create_app()) as fresh:
            self.assertEqual(len(fresh.get("/songs").json()), 3)
            self.assertEqual(fresh.get("/songs").json()[0]["votes"], 3)


if __name__ == "__main__":
    unittest.main()
