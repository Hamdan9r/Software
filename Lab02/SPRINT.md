# Sprint 1 — LabLoans

Planning assumption: one week, two developers and a provisional capacity of 14 relative points. Estimates and scope must be agreed with the actual team before execution. This file is a sprint plan, not evidence that software has been built.

## Sprint Goal

Give the lab technician a usable, authorized equipment checkout-and-return workflow with visibility of current loans, so the technician can tell which equipment is available and who holds each lent asset.

## Selected items

| Order | ID | Points | Sprint outcome | Dependency |
|---|---|---|---|---|
| 1 | LL-1 | 2 | Authorized staff can administer loans; others cannot. | Identity access agreed |
| 2 | LL-2 | 2 | Physical assets have unique registered IDs. | LL-1 |
| 3 | LL-3 | 3 | Checkout records one accountable open loan per asset. | LL-1, LL-2 |
| 4 | LL-4 | 2 | Return closes the loan and restores availability. | LL-3 |
| 5 | LL-5 | 3 | Staff see an accurate interactive current-loans list. | LL-3, LL-4 |
| 6 | LL-6 | 2 | The list marks overdue loans under the agreed due-date rule. | LL-5 |

Total: 2 + 2 + 3 + 2 + 3 + 2 = **14 points**, equal to the assumed capacity.

Sequence the loan state changes before the dependent list and overdue view. Demonstrate the full cycle using fictional borrower IDs and a small asset dataset. LL-7 and LL-8 remain unselected; they do not support the immediate staff workflow strongly enough to displace a selected item. If estimates grow, review LL-6 and LL-5 first rather than dropping authorization, return handling or acceptance checks.

## Definition of Done

Every selected item must meet all of the following before it is called Done:

- Its BACKLOG.md acceptance criteria pass, including authorization and applicable failure/empty-state cases.
- A reviewer checks the change for correctness, readable code and unnecessary scope.
- Relevant automated checks pass; checkout/return tests verify consistency and competing-checkout behaviour using fictional data.
- The increment runs from a clean checkout with documented setup, test and run commands; dependencies are declared and generated environments are not committed.
- Data access is restricted as agreed, no real borrower information or credentials enter test fixtures or repository history, and unresolved retention policy is flagged before a real-data pilot.
- The selected workflows are integrated; a demonstrated checkout and return leave the asset and loan records consistent.
- Changes and acceptance evidence are committed, and the technician review is ready. Record actual review feedback when it occurs; readiness for review is not stakeholder approval.

A partial implementation, unexecuted test, or merely written acceptance criterion is not Done. The definition applies to future implementation; these planning deliverables do not claim any item has passed it.
