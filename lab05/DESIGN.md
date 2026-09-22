# Campus Workshop Board - Design notes

Name: [enter your submission name]
Student ID: [enter your student ID]

## Diagram files

| View | Editable source (and page if needed) | Export |
|---|---|---|
| 01-context | [01-context.drawio](diagrams/source/01-context.drawio) | [01-context.svg](diagrams/exports/01-context.svg) |
| 02-containers | [02-containers.drawio](diagrams/source/02-containers.drawio) | [02-containers.svg](diagrams/exports/02-containers.svg) |
| 03-components | [03-components.drawio](diagrams/source/03-components.drawio) | [03-components.svg](diagrams/exports/03-components.svg) |
| 04-code | [04-code.drawio](diagrams/source/04-code.drawio) | [04-code.svg](diagrams/exports/04-code.svg) |
| 05-dynamic | [05-dynamic.drawio](diagrams/source/05-dynamic.drawio) | [05-dynamic.svg](diagrams/exports/05-dynamic.svg) |

Each source has one page; open it in diagrams.net. Each export is a standalone, scalable diagram.

## One structural choice (Exercise 2)

A server-rendered Board Web App and one PostgreSQL Board Database keep deployment simple for 200 students and one small team while database transactions protect shared reservation state.

## Your components (Exercise 3)

All six components run inside **Board Web App**; none is a separately deployed service.

| Name | Job | Customer rule(s) served |
|---|---|---|
| Web Endpoints | Handle HTTPS forms and pages; obtain verified identity, dispatch operations and render only authorised results. | R1, R2, R3, R4, R6 |
| Identity Gateway | Verify credentials with Campus Identity; issue and validate signed, expiring session cookies carrying verified student ID, name and email. | R1, R4 |
| Workshop Service | Validate creation, assign ID/owner, enforce owner-only publication and attendee access, and return published summaries with the caller's own reservation. | R2, R3, R5 |
| Reservation Rules | Reject unverified calls; preserve one seat per student and capacity under overlap; return existing reservations unchanged; request confirmation only after a new commit. | R1, R4, R6 |
| Persistence | Read/write workshops and reservations using PostgreSQL; supply locked transactions and fresh query results. | R2, R3, R4, R5 |
| Confirmation Gateway | Submit one confirmation to University Mail, mapping failure/timeout to Unavailable without undoing a reservation. | R6 |

## Reservation operation (Exercise 4)

See **04-code**, including its typed contract, ordered decision flow, and concurrency proof. The operation is `reserve(identity: AuthResult, workshopId: WorkshopId) -> ReserveResult`. All reservation writers lock the same workshop row, then check existing reservation and count in subsequent READ COMMITTED statements before insertion and commit. The invariant is `0 <= reservationCount(w) <= capacity(w)` and at most one reservation per `(workshopId, studentId)`. Only a new committed reservation triggers mail; an existing reservation is returned unchanged even when full.

## Ari's incident (Exercise 5)

| Observation | Result |
|---|---|
| Stored state before | W17 = “Build a tiny game”, owner S10, published, capacity 3, start time unchanged. Reservations belong to S21 and S22 (2 seats); S23 has none. Remaining seats = 1. |
| Stored state after | W17 and S21/S22 reservations are unchanged. One new reservation R23 (illustrative generated ID) belongs to S23, with verified name Ari and email ari@example.invalid; total = 3 and remaining = 0. The seat is committed before mail is attempted. Mail failure causes no rollback or extra reservation. |
| Message Ari sees | **“Your reservation for ‘Build a tiny game’ succeeded, but email is unavailable.”** The receipt shows Ari's own reservation R23. A subsequent browse/refresh reads the same stored reservation and 0 remaining seats. Ari cannot see other attendees' names or emails. |
