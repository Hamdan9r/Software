# Lab 04 report

Student name: [Enter your name]

Date of automated verification: 2026-09-15

Repository: https://github.com/Hamdan9r/Software (folder: `Lab04`, branch: `main`).
This existing repository is public; the sheet requests a private `ai1220` repository.

Status: Code completed with Codex assistance. Automated backend and JavaScript
request checks passed. Browser verification and personal details remain pending. Git publication is
recorded in the Submission section.
The observations below were produced by Codex in this execution environment;
they are not claimed as personal browser observations. Review the explanations
and add your own observations before submission.

## Exercise 1 - Explore and make a commit

- Working folder: the session started at `/workspace/scratch/85adba6b40e8`.
  Completed files are in its `lab04/` folder. The required local destination is
  `lab04/` inside the student's existing `ai1220` repository.
- Git repository root: unavailable here. `git rev-parse --show-toplevel`
  reported that the working folder was not a Git repository.
- Initial report commit hash (`Start lab04 report`): aa169baf81064c7f2e450cf6f80854a61706ac19.
  This report-only snapshot was created during publication, after implementation;
  it does not claim the original Exercise 1 ordering was followed.
- Files included in that commit: only `Lab04/REPORT.md`.
- What was saved in that commit: the prepared report with implementation
  explanations, automated observations, and explicit pending personal/browser
  work. The subsequent completion commit records the initial snapshot hash.
- Playlist ownership: `backend.py` owns the `songs` list and `next_id`. The
  server assigns IDs and decides whether an addition is valid. The list lives
  in the Python process, so stopping and restarting it restores the seed data.
- Playlist display: `index.html` supplies the page and JavaScript. Its
  `loadSongs()` function builds a list item for each song returned by the server.
- Initial loading: the browser requests `/` for the HTML. The page calls
  `loadSongs()`, which uses `requestJSON("/songs")` to perform a GET. The server
  returns the songs as JSON. JavaScript parses that response and displays each
  title and artist using `textContent`.
- Initial starter check: before editing, `GET /` returned 200 and contained the
  starter heading. `GET /songs` returned 200 with only
  `{"id": 1, "title": "First Light", "artist": "Demo Band"}`.
- Access limitations: the student's repository and name were not supplied. A
  browser executable was unavailable and its download was blocked by network
  restrictions. Instructor assistance has not been recorded. The uploaded
  README identifies these files as a recreated starter; the original course
  ZIP was not provided.

## Exercise 2 - Backend

`create_song(payload)` checks `title` and `artist` in a loop. `payload.get(field)`
returns `None` when a field is absent, which fails the string check. Each string
is trimmed using `strip()`, then its length must be between 1 and 80 inclusive.
Invalid input raises `ValueError` with the field name and a helpful explanation.
The supplied HTTP handler turns that error into a 400 JSON response.

The cleaned strings are first collected in a local dictionary. Only after both
fields pass validation does the function build a song using the current
`next_id`, append it to `songs`, increment `next_id`, and return the song.
`global next_id` allows the assignment to update the module-level counter.
This ordering prevents a rejected artist from leaving a partially stored song
or consuming an ID. Extra payload fields are never copied into the song.
Appending preserves insertion order; no duplicate-title restriction is added.

Before editing the frontend, actual direct HTTP checks showed:

- Accepted: `{"title":"  Quiet Road  ","artist":"Sample Artist"}` returned
  201 and `{"id":2,"title":"Quiet Road","artist":"Sample Artist"}`.
- Rejected: `{"title":"   ","artist":"Sample Artist"}` returned 400 and
  `{"error":"Title must contain 1 to 80 characters after trimming."}`.
- After rejection, the list still contained only the seed and Quiet Road, and
  `next_id` remained 3. These values were checked directly with assertions.

## Exercise 3 - Frontend

- Visible heading in the HTML: `My playlist`.
- `sendSong(title, artist)` returns `requestJSON("/songs", options)`. Its options
  set `method` to `POST`, the `Content-Type` header to `application/json`, and
  the body to `JSON.stringify({ title, artist })`.
- The path, method, field names, header, and JSON body match the contract. The
  raw input strings are sent unchanged; trimming and validation happen in
  Python. Returning the helper's promise lets the form handler await the
  stored song or catch the server's error.
- The supplied form handler should reset the inputs after an accepted POST,
  then call `loadSongs()` to fetch and display the server's stored list. On
  rejection it should show the error and return before resetting or reloading.
  These are code-reviewed behaviors; browser observations remain pending.
- Actual function integration: the page's real `requestJSON` and `sendSong`
  functions were extracted and run in Node against the live Python server.
  Blue Sky / Test Duo returned ID 2. Padded Moon Walk / Sample Trio returned
  trimmed values with ID 3. A whitespace-only title threw the server's error,
  and the following GET was identical to the previous GET. Correcting the
  title succeeded with ID 4. No browser or simulated visual result is claimed.
- Display/data comparison: pending in the browser. Compare the visible list
  against `GET /songs` in Developer Tools or a direct request.

## Exercise 4 - Actual verification observations

“Partial” means the underlying request or data was checked, but the required
browser behavior still needs observation. There were no failed automated
assertions. The API suite recorded 29 checks; a separate JavaScript integration
run exercised the actual request functions and a full server-process restart.

| Check from page 3 | Actual observation | Result |
| --- | --- | --- |
| Fresh start: page and GET show only seed, ID 1 | GET returned the single seed song; HTML returned 200 with the new heading. Rendered list not checked. | Partial |
| Form: Blue Sky / Test Duo appears once; fields clear | Actual `sendSong` returned 201 with ID 2; next GET contained two songs. Form display and clearing not checked. | Partial |
| Refresh: both songs remain | Repeated GET retained stored songs. Browser refresh not checked. | Partial |
| Form: another invented song works | Actual `sendSong` accepted padded Moon Walk / Sample Trio with ID 3 and trimmed values. Form not checked. | Partial |
| Direct addition: 201, trimmed values, next ID; visible after refresh | Fresh API server returned Quiet Road / Sample Artist with ID 2, ignoring supplied ID 999 and an extra field. Browser visibility pending. | Partial |
| Whitespace-only title: 400; no new song | Returned helpful 400; song list and next ID matched their pre-request values. | Pass |
| Missing artist: 400 | Returned `Artist must be present and must be a string.`; state unchanged. | Pass |
| Numeric title: 400 | Returned `Title must be present and must be a string.`; state unchanged. | Pass |
| 81-character title: 400 | Rejected with a length error; state unchanged. | Pass |
| 80-character title: accepted | 80-character title and artist together returned 201 with ID 3 after all rejections in the API run. | Pass |
| Rejected additions do not consume an ID | Every invalid API request preserved `next_id`; next successful addition received ID 3. | Pass |
| Form rejection: error, retained inputs, unchanged list | Actual request function propagated the error; GET data was unchanged. Visual message and retained inputs pending. | Partial |
| Corrected form submission succeeds | Corrected actual `sendSong` call returned 201 with ID 4. Form interaction pending. | Partial |
| Keyboard: Tab and Enter work | No browser executable available; not run. | Pending |
| Network: POST payload, 201, JSON response, following GET | Instrumented real fetch calls verified these values and a following GET. Manual Developer Tools inspection pending. | Partial |
| Restart and refresh: only seed remains | Stopped and restarted the actual Python process; GET returned only the seed. Browser refresh pending. | Partial |

Additional API assertions passed for both fields: missing, numeric, null,
boolean, list, object, empty string, whitespace-only, and 81-character values
were rejected. Both 1-character fields were accepted. Both fields were trimmed.
Duplicate titles were accepted. GET preserved insertion order. Malformed JSON,
non-object bodies, and invalid UTF-8 returned 400 through the unchanged handler;
unknown GET and POST paths returned 404.

### One successful request and response

Captured during Exercise 2, before frontend edits, from a fresh server.

Request method and path: `POST /songs`

Request header: `Content-Type: application/json`

Actual request body:

```json
{"title": "  Quiet Road  ", "artist": "Sample Artist"}
```

Actual response status: `201 Created`

Actual response headers (selected):

```text
Content-Type: application/json
Content-Length: 59
Cache-Control: no-store
```

Actual response body:

```json
{"id": 2, "title": "Quiet Road", "artist": "Sample Artist"}
```

The server list contained the seed and this stored song; `next_id` was 3.
A separate API run confirmed GET returned stored songs in insertion order.
The browser page was not visually checked.

### One failed request and response

Captured immediately after the accepted Exercise 2 request above.

Request method and path: `POST /songs`

Request header: `Content-Type: application/json`

Actual request body:

```json
{"title": "   ", "artist": "Sample Artist"}
```

Actual response status: `400 Bad Request`

Actual response headers (selected):

```text
Content-Type: application/json
Content-Length: 66
Cache-Control: no-store
```

Actual response body:

```json
{"error": "Title must contain 1 to 80 characters after trimming."}
```

An assertion confirmed that the seed and Quiet Road were still the only songs
and `next_id` was still 3. The broader API run compared both state values before
and after every rejection, then confirmed the next accepted song received ID 3.

### One code change to review and explain

File and change: in `backend.py`, both fields are validated into a local
`cleaned` dictionary before appending to `songs` or incrementing `next_id`.

Explanation: validating the title alone is insufficient. If the artist is
invalid, adding the song or incrementing the counter too early would break the
contract. Delaying both mutations until validation is complete keeps rejected
requests from changing shared state.

Observed result: missing and invalid artists returned 400 while the song list
and ID counter remained exactly unchanged. The next valid request received the
next unused ID. This agrees with the contract's rejection and ID requirements.

Student review: [Review this change and confirm you can explain it in your own words.]

## Submission

- Required files prepared: `backend.py`, `index.html`, `REPORT.md`, `README.md`,
  and `.gitignore`.
- Personal details: student name and review still required; repository identified above.
- Initial commit: report-only snapshot made during publication after implementation,
  as documented above. The original before-implementation sequence was not performed.
- Completion commit: `Complete lab04 playlist`; obtain its hash from the
  [Lab04 history](https://github.com/Hamdan9r/Software/commits/main/Lab04).
  Its own hash cannot be embedded in the contents of that same commit.
- Files included and review notes: the five required files in `Lab04/`. Code changes are
  confined to `create_song`, `sendSong`, and the requested heading/comment.
  The supplied HTTP handler, form handling, and display functions are unchanged.
- Git publication: committed directly through the connected GitHub account to
  `Hamdan9r/Software`, branch `main`, folder `Lab04`. This used GitHub operations,
  rather than a local terminal `git push`. Earlier repository-access limitations
  describe the implementation session; access became available during publication.
- Browser checks: complete all Partial/Pending items above and replace them
  with actual observations before submission.
- Optional stretch: not attempted.
