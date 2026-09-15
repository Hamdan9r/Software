# Lab 04 - Frontend and Backend

The playlist implementation is complete. It uses Python's standard library and
an HTML page with JavaScript; no Python packages or API key are needed.

These files are based on the uploaded recreated starter. Its original README
states that the course's original `lab04_files.zip` was not supplied. Confirm
with your instructor if the original starter is required.

## Run

1. Clone or pull the `Hamdan9r/Software` repository.
2. Open a terminal in `Software/Lab04/`.
3. Run `python3 backend.py` (Windows: `py backend.py`).
4. Open <http://127.0.0.1:8000/> in your browser.

Keep the terminal open. Stop with Ctrl+C. Restart after Python changes; refresh
after HTML changes. Restarting resets the playlist to First Light / Demo Band.
Use Python 3.10 or newer.

## Completed changes

- `backend.py`: `create_song(payload)` validates both fields, trims surrounding
  whitespace, stores accepted songs, assigns consecutive IDs, and raises
  `ValueError` for rejected additions without modifying state.
- `index.html`: the heading is `My playlist`; `sendSong(title, artist)` sends the
  raw form values through `requestJSON` to `POST /songs` as JSON.
- `REPORT.md`: explanations and actual automated test observations are filled
  in. Personal details and browser checks are explicitly pending.
- `.gitignore`: excludes Python caches and local virtual environments.

The supplied HTTP handler, form handler, and list-rendering logic are unchanged.

## API contract

| Request | Response |
| --- | --- |
| `GET /` | 200 and the HTML page |
| `GET /songs` | 200 and the playlist in insertion order |
| Valid `POST /songs` | 201 and the stored song with its assigned integer ID |
| Invalid addition | 400 and a JSON `error`; no playlist or ID change |

Both `title` and `artist` must be strings, with 1-80 characters after trimming.
Extra fields are ignored and duplicate titles are allowed. IDs begin at 1;
the seed uses ID 1 and the first addition receives ID 2. Data is in memory only.

## Verification already performed

29 API checks passed, covering both fields, trimming, valid length boundaries,
invalid types and lengths, missing fields, unchanged state after rejection,
ignored extra fields, duplicates, insertion order, malformed requests, and
unknown paths. The real JavaScript `requestJSON` and `sendSong` functions were
also executed in Node against the live Python HTTP server; successful and
failed requests, returned errors, assigned IDs, and a server restart passed.

These are automated HTTP and function checks. This environment could not run
a browser, so visual behavior, keyboard access, and Developer Tools inspection
still require the checks below. See `REPORT.md` for the exact distinction.

## Finish the browser checks

Use invented song data and record your actual observations in `REPORT.md`.

1. Restart and open the page. Confirm only First Light / Demo Band appears.
2. Add Blue Sky / Test Duo. Confirm it appears once and both inputs clear.
3. Refresh: both songs should remain. Add Moon Walk / Sample Trio.
4. In a second terminal, run:

   ```bash
   curl -i http://127.0.0.1:8000/songs \
     -H 'Content-Type: application/json' \
     -d '{"title":"  Quiet Road  ","artist":"Sample Artist"}'
   ```

   Confirm 201, trimmed values, and the next ID. Refresh to see the song.
5. Try the invalid direct request:

   ```bash
   curl -i http://127.0.0.1:8000/songs \
     -H 'Content-Type: application/json' \
     -d '{"title":"   ","artist":"Sample Artist"}'
   ```

   Confirm 400 and no new song.
6. In the form, submit a title containing only spaces with a nonempty artist.
   Confirm an error appears, the inputs remain, and the displayed list is
   unchanged. Correct the title and submit successfully.
7. Use Tab to move through Title, Artist, and Add song. Use Enter to submit.
8. In browser Developer Tools > Network, inspect the successful `POST /songs`
   JSON payload, status 201, and response, then the following `GET /songs`.
   Compare the returned list with the page.
9. Stop and restart the server, then refresh. Only the seed song should remain.

## Repository and submission

This lab is stored in [Hamdan9r/Software, Lab04](https://github.com/Hamdan9r/Software/tree/main/Lab04),
alongside the existing labs. `Lab04` follows this repository's naming convention;
the course sheet calls the destination `ai1220/lab04` and asks for a private
repository. The existing connected `Software` repository is public. Confirm the
required repository and folder naming with your instructor before submission.

The upload history uses a report-only `Start lab04 report` commit followed by
`Complete lab04 playlist`. The report-only snapshot was made after the code was
implemented; it does not establish that Exercise 1 preceded implementation.

Fill in your name, review the explanations, and complete the browser checks in
`REPORT.md`. These personal observations remain unfinished. For later edits,
from the repository root:

```bash
git status --short
git diff -- Lab04
git add -- Lab04/backend.py Lab04/index.html Lab04/REPORT.md Lab04/README.md Lab04/.gitignore
git commit --only -m "Record lab04 browser verification" -- Lab04/backend.py Lab04/index.html Lab04/REPORT.md Lab04/README.md Lab04/.gitignore
git push
```

Inspect the commit contents and verify the updated files on GitHub.
