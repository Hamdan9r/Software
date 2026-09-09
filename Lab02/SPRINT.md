# Sprint 1 — LabLoans

Planning assumption: one week, two developers and a provisional capacity of 14 relative points. Estimates and scope must be agreed with the actual team before execution. This file is a sprint plan, not evidence that software has been built.

## Sprint Goal

Give the lab technician a usable, authorized equipment checkout-and-return workflow and a repeatable weekly report of every open loan, so the technician can account for equipment before and during exams.

## Selected items

| Order | ID | Points | Sprint outcome | Dependency |
|---|---|---|---|---|
| 1 | LL-1 | 2 | Authorized staff can administer loans; others cannot. | Identity access agreed |
| 2 | LL-2 | 2 | Physical assets have unique registered IDs. | LL-1 |
| 3 | LL-3 | 3 | Checkout records one accountable open loan per asset. | LL-1, LL-2 |
| 4 | LL-4 | 2 | Return closes the loan and restores availability. | LL-3 |
| 5 | LL-9 | 5 | Staff obtain a complete, cutoff-based weekly open-loan report. | LL-1, LL-3, LL-4 |

Total: 2 + 2 + 3 + 2 + 5 = **14 points**, equal to the assumed capacity.

Sequence authorization and asset registration before checkout/return, then build LL-9 on the completed loan lifecycle. Plan 3 points for consistent report generation and 2 for scheduling, retries and status. Demonstrate a cutoff with an older open loan, a not-yet-overdue loan, a loan returned before the cutoff, a loan returned after it, and a checkout after the cutoff; only the correct three open-at-cutoff loans appear.

Change from the baseline: LL-5 (3 points) and LL-6 (2 points) are removed to accommodate LL-9 (5 points). The interactive current-loans screen and overdue highlighting remain Should items for a later sprint. LL-7 and LL-8 remain unselected. The actual implementation team must re-estimate LL-9; if it exceeds 5 points, renegotiate the scope/date explicitly instead of silently overloading the sprint or removing integrity checks.

Scheduling assumption: first report by the end-of-week-1 review, with weekly Monday 09:00 Asia/Dubai cutoff thereafter; confirm the exact first cutoff and exam date with the technician. This is a proposal, not a verified exam deadline. Keep both scheduled generation and authorized manual rerun in LL-9 acceptance.

## Definition of Done

Every selected item must meet all of the following before it is called Done:

- Its BACKLOG.md acceptance criteria pass, including authorization and applicable failure/empty-state cases.
- A reviewer checks the change for correctness, readable code and unnecessary scope.
- Relevant automated checks pass; checkout/return tests verify consistency and competing-checkout behaviour using fictional data.
- The increment runs from a clean checkout with documented setup, test and run commands; dependencies are declared and generated environments are not committed.
- Data access is restricted as agreed, no real borrower information or credentials enter test fixtures or repository history, and unresolved retention policy is flagged before a real-data pilot.
- The selected workflows are integrated; a demonstrated checkout and return leave the asset and loan records consistent.
- The report acceptance checks cover every open-at-cutoff loan, zero rows, permission boundaries, generation failure, retry without duplicates, and concurrent loan changes. Scheduled and manual generation agree for the same cutoff.
- Changes and acceptance evidence are committed, and the technician review is ready. Record actual review feedback when it occurs; readiness for review is not stakeholder approval.

A partial implementation, unexecuted test, or merely written acceptance criterion is not Done. The definition applies to future implementation; these planning deliverables do not claim any item has passed it.
