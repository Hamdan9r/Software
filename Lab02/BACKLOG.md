# Backlog — LabLoans

This baseline uses the explicitly assumed product boundary in PLAN.md. Rank is execution/value order; points are relative estimates. Must means required for the proposed usable loan cycle; Should and Could can be deferred. No feature is claimed to be implemented.

## Items

| Rank | ID | Priority | Points | Item and value | Depends on |
|---|---|---|---|---|---|
| 1 | LL-1 | Must | 2 | As a technician, I want staff-only loan administration so only authorized people can alter equipment records. | Confirm institutional identity access |
| 2 | LL-2 | Must | 2 | As a technician, I want a register of uniquely identified assets so checkout refers to the correct physical item. | LL-1 |
| 3 | LL-3 | Must | 3 | As a technician, I want to record a checkout and borrower so every lent asset is accountable. | LL-1, LL-2 |
| 4 | LL-4 | Must | 2 | As a technician, I want to record returns so returned equipment can be lent again. | LL-3 |
| 5 | LL-5 | Should | 3 | As a technician, I want an interactive list of current loans so I can answer a desk query quickly. | LL-3, LL-4 |
| 6 | LL-6 | Should | 2 | As a technician, I want overdue loans highlighted so I can prioritize follow-up. | LL-5; confirm due-date policy |
| 7 | LL-7 | Could | 3 | As a borrower, I want to see my own loans so I can check what I need to return. | LL-1, LL-3, LL-4; borrower role |
| 8 | LL-8 | Could | 2 | As a technician, I want an asset's loan history so I can investigate an earlier transaction. | LL-3, LL-4; approved retention policy |

Acceptance criteria:

### LL-1

- Given an authorized staff identity, when staff sign in, then asset and loan administration is available.
- Given an anonymous user or a borrower without staff authorization, when they request a loan-changing operation directly, then access is denied and no record changes.

### LL-2

- Given staff authorization, when a new unique asset ID and name are saved, then the asset is available for checkout selection.
- Given an existing asset ID, when staff try to register it again, then the duplicate is rejected without changing the original asset.

### LL-3

- Given an available registered asset and valid borrower ID, when staff complete a checkout, then exactly one open loan records the asset, borrower, checkout time and due date, and the asset becomes unavailable.
- Given two competing checkout requests for the same asset, when both execute, then exactly one succeeds and the other reports unavailability; only one open loan exists.
- Given an unknown borrower/asset or failed save, when checkout is attempted, then it fails without leaving a partial loan or an unavailable asset with no loan.

### LL-4

- Given an open loan, when staff confirm the return, then that loan receives a return timestamp and the asset becomes available in the same completed operation.
- Given an already returned loan, when return is submitted again, then no second return or unrelated loan change is created.

### LL-5

- Given open and returned loans, when staff open the current-loans screen, then each open loan appears once and returned loans are absent.
- Given a return just saved, when the screen is refreshed, then the returned loan is absent; with no open loans it displays an explicit empty state.

### LL-6

- Given an open loan with a due date earlier than the current date in the agreed campus timezone, when the current-loans screen is shown, then the loan is marked overdue.
- Given a loan due today or a returned loan, when the overdue condition is evaluated, then it is not marked overdue under this proposed date-based rule.

### LL-7

- Given a signed-in borrower, when they open their loans, then only their own current loans are visible.
- Given another borrower's loan identifier, when they attempt direct access, then the record is denied.

### LL-8

- Given an authorized technician and an asset with permitted retained loan records, when the asset history is opened, then records appear by checkout time with return state.
- Given a borrower without staff authorization, when they request the asset's staff history, then access is denied.

Out of the proposed first release: reservations, payments/fines, a native mobile app, and automated borrower messaging. These are scope assumptions, not exclusions quoted from the unavailable brief.

## The change

Baseline version: the change is not yet incorporated into backlog or sprint scope. The change notes were already seen during the initial scan, as disclosed in PLAN.md; this section does not claim they remained unread. The later change commit will explicitly record the delta from this baseline.

## From the assistant

Kept:

- The suggestion to deliver checkout and return together: LL-3 without LL-4 would leave the first increment unable to complete a normal loan cycle.
- Separate negative-path criteria for unauthorized changes and competing checkouts, because a visually working screen alone would not protect loan integrity.
- A small backlog with explicit dependencies and a capacity limit, so later reprioritization has a visible cost.

Rejected:

- Building reservations or automatic fines in the first increment: neither is supported by the available scenario evidence and both would expand the workflow.
- Treating effort points as hours or claiming that a capacity estimate proves the sprint is feasible; there is no measured velocity.
- Describing these documents as stakeholder-approved or as a full solution to a rubric that was not available. The missing brief and assumptions remain visible.

These are decisions from the assistant-assisted planning review, not a claim that the technician or student conducted an external review.
