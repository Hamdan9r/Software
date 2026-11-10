# Playlist API contract

The page and API share one origin. All fields use snake_case. Songs remain in
insertion order. Each fresh server starts with the three songs below; data is
stored in memory and resets when the server restarts.

## 1. Get all songs

Method: GET

Path: /songs

Request body: none

Response status: 200

Response body (the three starting songs):
```json
[
  {"id": 1, "title": "Blue Monday", "artist": "New Order", "votes": 3},
  {"id": 2, "title": "Clocks", "artist": "Coldplay", "votes": 1},
  {"id": 3, "title": "Dancing Queen", "artist": "ABBA", "votes": 0}
]
```

## 2. Add a song

Method: POST

Path: /songs

Request body:
```json
{"title": "Yellow", "artist": "Coldplay"}
```

Response status: 201

Response body:
```json
{"id": 4, "title": "Yellow", "artist": "Coldplay", "votes": 0}
```

The response is the newly stored song. Its id is the next unused integer and
votes starts at 0. Title and artist must be strings with non-whitespace content;
surrounding whitespace is removed. Additional request fields are ignored.

Error status (title or artist missing or empty): 400

Error body:
```json
{"error": "Title and artist are required."}
```

Non-string fields and non-object JSON use the same error. Malformed JSON returns
400 with `{"error": "Request body must be valid JSON."}`. Rejected requests do
not store a song or consume an id.

## 3. Vote for a song

Method: POST

Path (write the song's id as {id}): /songs/{id}/vote

Request body: none

Response status: 200

Response body (voting for song 1 once on a fresh server):
```json
{"id": 1, "title": "Blue Monday", "artist": "New Order", "votes": 4}
```

The response is the updated song. Each successful request increments its votes
by one, without changing the playlist order.

Error status (no song with that id): 404

Error body (for id 99999):
```json
{"error": "There is no song 99999"}
```

The error message contains the requested id. All refusals use the same
`{"error": "message"}` structure.
