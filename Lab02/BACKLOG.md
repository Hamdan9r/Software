# Backlog — LabLoans

This revised backlog uses the explicitly assumed product boundary in PLAN.md. Rank is execution/value order; points are relative estimates. Must means required for the proposed usable loan cycle; Should and Could can be deferred. No feature is claimed to be implemented.

## Items

| Rank | ID | Priority | Points | Item and value | Depends on |
|---|---|---|---|---|---|
| 1 | LL-1 | Must | 2 | As a technician, I want staff-only loan administration so only authorized people can alter equipment records. | Confirm institutional identity access |
| 2 | LL-2 | Must | 2 | As a technician, I want a register of uniquely identified assets so checkout refers to the correct physical item. | LL-1 |
| 3 | LL-3 | Must | 3 | As a technician, I want to record a checkout and borrower so every lent asset is accountable. | LL-1, LL-2 |
| 4 | LL-4 | Must | 2 | As a technician, I want to record returns so returned equipment can be lent again. | LL-3 |
| 5 | LL-9 | Must | 5 | As a lab technician, I want a weekly report of every open loan so I can account for equipment during exam weeks. | LL-1, LL-3, LL-4 |
| 6 | LL-5 | Should | 3 | As a technician, I want an interactive list of current loans so I can answer a desk query quickly. | LL-3, LL-4 |
| 7 | LL-6 | Should | 2 | As a technician, I want overdue loans highlighted so I can prioritize follow-up. | LL-5; confirm due-date policy |
| 8 | LL-7 | Could | 3 | As a borrower, I want to see my own loans so I can check what I need to return. | LL-1, LL-3, LL-4; borrower role |
| 9 | LL-8 | Could | 2 | As a technician, I want an asset's loan history so I can investigate an earlier transaction. | LL-3, LL-4; approved retention policy |

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

### LL-9

- Given a reporting cutoff T, when the weekly report is generated, then it contains each loan checked out at or before T and not returned at or before T exactly once, with loan ID, asset ID/name, borrower university ID, checkout time and due date. It includes all open loans, not only overdue loans; a return after T does not remove a loan that was open at T.
- Given a report, when staff open it, then the cutoff timestamp, campus timezone, generation time and total open-loan count are shown; the count equals the number of loan rows. An empty period produces an explicit zero-open-loan report.
- Given the configured weekly schedule, when the cutoff arrives, then a report is generated and made available to authorized staff; a non-staff user cannot view or download it by direct link.
- Given a transient generation failure, when the job retries or staff rerun the same cutoff, then one successful report is published for that cutoff without duplicate loan rows or duplicate published reports. Until success, staff see a failure/pending state, not an empty or partial report presented as complete.
- Given an authorized manual run for a specified cutoff, when staff request the report, then it uses the same snapshot rules as the scheduled report and is available as a staff-only downloadable CSV. A consistent cutoff snapshot prevents concurrent checkout/return from changing membership halfway through generation.

Assumed LL-9 design details: Monday 09:00 Asia/Dubai cutoff, in-service access, CSV download and the listed fields. The source asks for a weekly report but supplies none of those details; confirm them with the technician. The 5-point estimate includes snapshot/report generation (3) and scheduling/retry/status behaviour (2), not only a screen.

Out of the proposed first release: reservations, payments/fines, a native mobile app, and automated borrower messaging. These are scope assumptions, not exclusions quoted from the unavailable brief.

## The change

Source: `sealed/change-C-labloans.md`. The lab technician reports that most equipment goes missing during exam weeks and requests a weekly report of **every open loan**, with exams approaching.

Response: add LL-9 as Must, rank it immediately after the data-integrity prerequisites, and pull it into Sprint 1. Keep LL-1–LL-4 because a report built on unauthorized or inconsistent checkout/return data would be unreliable. Move LL-5 (3 points) and LL-6 (2 points) out of Sprint 1 to make room for LL-9 (5 points); retain them as Should backlog items. Capacity remains 14 points. The revised goal delivers an accountable loan cycle and the weekly report before optional interactive views.

The change is not solved by merely relabeling the live loan list: LL-9 adds a time-specific snapshot, weekly scheduling, an explicit empty report, restricted download and failure/retry behaviour. The existing loan and return timestamps support the cutoff calculation. A borrower self-service page, reminders or fines would not satisfy the technician's request.

Unknowns: exact exam date, first required report date, weekly cutoff/timezone, recipients, minimum report fields and report retention. Ask the technician before promising a date. If the first deadline falls before the assumed week's end, negotiate a smaller first increment or an authorized manual report process using the same criteria; do not claim the assumed sprint meets an unknown deadline.

Process disclosure: the initial scan read the sealed note before the baseline commits. Those commits precede incorporation of LL-9, but they do not prove a genuinely unseen change. This is documented here and in PLAN.md rather than disguising the order.

## From the assistant

Kept:

- The suggestion to deliver checkout and return together: LL-3 without LL-4 would leave the first increment unable to complete a normal loan cycle.
- Separate negative-path criteria for unauthorized changes and competing checkouts, because a visually working screen alone would not protect loan integrity.
- The recommendation to add the requested weekly report while removing equal estimated effort from lower-priority work, rather than increasing capacity without evidence.
- A small backlog with explicit dependencies and a capacity limit, so later reprioritization has a visible cost.

Rejected:

- Adding only an overdue report: the technician asked for every open loan, including loans that are not overdue.
- Building reservations or automatic fines in the first increment: neither is supported by the available scenario evidence and both would expand the workflow.
- Treating effort points as hours or claiming that a capacity estimate proves the sprint is feasible; there is no measured velocity.
- Describing these documents as stakeholder-approved or as a full solution to a rubric that was not available. The missing brief and assumptions remain visible.

These are decisions from the assistant-assisted planning review, not a claim that the technician or student conducted an external review.
