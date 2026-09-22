# Lab 5 - C4 Design Challenge

90 minutes. Work individually in `lab05/` inside your existing private `ai1220` repository.

Read the two-page student sheet. Produce four C4 views and one dynamic diagram for the Campus Workshop Board. No application code or long report is required.

1. Copy this folder's contents into `ai1220/lab05/` without creating a nested repository.
2. Use any diagramming tool. Save editable files in `diagrams/source/` and readable PDF/SVG/PNG exports in `diagrams/exports/`.
3. Follow the five questions in the sheet. Use `DESIGN.md` only for the brief notes and component list; the diagrams carry the explanation.
4. Check consistency and readability. Commit and push before the session ends, then verify files and instructor access on GitHub.

Weights: context 15%, containers 20%, components 25%, code 15%, dynamic 25%. Partial work earns proportional credit.

AI assistance is allowed; check and understand its output. No paid service, real credentials or application setup is needed. If tooling or submission fails, save locally and ask the instructor for help before the session ends.

References: [C4 views](https://c4model.com/diagrams), [dynamic diagrams](https://c4model.com/diagrams/dynamic), [notation](https://c4model.com/diagrams/notation).

## Completed views

- [01 - System context](diagrams/exports/01-context.svg)
- [02 - Containers](diagrams/exports/02-containers.svg)
- [03 - Components](diagrams/exports/03-components.svg)
- [04 - Code](diagrams/exports/04-code.svg)
- [05 - Ari's reservation incident](diagrams/exports/05-dynamic.svg)

[DESIGN.md](DESIGN.md) contains the required short notes and source/export mapping. Open editable `.drawio` sources in diagrams.net. Open SVG exports in a browser and zoom as needed.

The proposed locking protocol follows PostgreSQL's [row-lock behaviour](https://www.postgresql.org/docs/current/explicit-locking.html#LOCKING-ROWS) and [READ COMMITTED statement snapshots](https://www.postgresql.org/docs/current/transaction-iso.html#XACT-READ-COMMITTED). External HTTPS/JSON APIs are design assumptions because the brief does not specify university API contracts.
