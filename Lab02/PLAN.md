# Plan — LabLoans

Name: Hamdan Alameri

## Process choice

### How stable and binding are the requirements?

The available material consists of PLAN, BACKLOG and SPRINT templates plus three change notes. The Lab 2 task sheet and original product briefs were not available. Following the instruction to proceed, this plan selects LabLoans. The baseline below is a proposed equipment-loan service, not a quotation from a missing brief. It needs confirmation against the task sheet before claiming full rubric compliance.

Assumed baseline: a lab technician records equipment checkout and return, identifies the borrower, and can determine which equipment remains on loan. Each physical asset has a unique identifier and at most one open loan. University users already have institutional identities. Checkout/return correctness and staff access are release constraints; the convenience features and workflow are negotiable assumptions.

### How quickly can real feedback arrive?

Assume one technician can review a small working increment each week and answer a short workflow question within two working days. Demonstrate an actual checkout followed by a return, using fictional data, before extending the interface. Confirm these availability assumptions at kickoff; if reviews are unavailable, agree written acceptance examples and a named substitute reviewer rather than silently accepting the work.

### What does failure cost?

A duplicate checkout, lost return, or inaccurate borrower record can make equipment unaccountable and delay student work. Exposed borrower identities are a privacy failure. Give transaction integrity, authorization and recovery priority over convenience. No monetary loss estimate or institutional compliance policy was supplied; ask the technician and university data owner rather than inventing one.

### How many pieces must move together?

The assumed first release has a staff-facing browser interface, university identity, an asset register and persistent loan records. Checkout must update availability and the loan together; a return must close the correct loan without losing history. These dependencies justify agreeing identifiers and state transitions early, but do not require designing every optional screen before obtaining feedback. Identity-service access is an external dependency to confirm.

Verdict:

Use iterative, incremental delivery with a prioritized backlog, one-week sprints, a technician review, and a short retrospective. Stable integrity and authorization rules get explicit acceptance checks; changing workflow details are reviewed through small increments. This suits uncertain requirements and assumed weekly feedback better than committing all optional features before seeing a usable loan cycle. Use only a lightweight Scrum-style planning cadence: the team size, roles and meeting availability have not been supplied, so this is not a claim that a complete Scrum team already exists.

## Milestones

All dates are relative planning assumptions, not completed activities. Assume two developers and a provisional Sprint 1 capacity of 14 relative effort points; estimates are planning judgments, not measured velocity.

| Milestone | When | What is true then |
|---|---|---|
| Confirm baseline and data | Before Sprint 1 | Technician confirms the minimum loan cycle, identity source, asset IDs, borrower identifiers, retention/access policy and demonstration dataset. |
| Complete a usable loan cycle | End of week 1 | Authorized staff can check out and return a registered asset; duplicate checkout and unauthorized changes are rejected; acceptance checks and a technician demo are ready. |
| Review the increment | End of week 1 review | Technician inspects fictional checkout/return examples and the selected visibility features; feedback changes the backlog, with no claim of approval until the review occurs. |
| Pilot and improve | Week 2, if review accepts readiness | An agreed small asset set is used under technician supervision; failures and recovery are reviewed before expanding use. |

## Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| Missing original brief leads to the wrong scope | High | Label the baseline as assumed; compare these files with the task sheet and assigned product before claiming course acceptance. |
| Technician cannot review weekly | Medium | Book the first review at kickoff and nominate a substitute; record unresolved decisions. |
| Two staff check out the same asset simultaneously | Medium | Enforce one open loan per asset atomically and test competing checkout requests. |
| University identity integration is unavailable | Medium | Verify access in week 0; use a clearly marked local test identity adapter only for demonstrations, never as production authentication. |
| Borrower records are exposed or kept too long | Medium | Restrict access to authorized staff, use fictional test data, and confirm a minimum data inventory and retention policy before a pilot. |
| A failed save loses or partially updates a loan | Medium | Commit asset/loan changes together; preserve the previous state after a failed transaction and verify backup/restore. |
| Estimates exceed the team's actual capacity | Medium | Re-estimate with the people doing the work and remove low-priority items before the sprint starts. |

## Assumptions, questions and provenance

- A1: Browser-based staff workflow, institutional identities and a persistent asset register are assumed product choices.
- A2: A loan contains an asset ID, borrower university ID, checkout time, agreed due date and optional return time. Whether due dates or multiple physical units are required must be confirmed.
- A3: One week, two developers, weekly review and 14 points are planning assumptions. Points are relative effort, not days or hours.
- Q1: Which original Lab 2 product brief and rubric apply, and which scenario was assigned?
- Q2: Who can authorize a checkout/return, which borrower attributes are necessary, and what retention and recovery policies apply?
- Q3: What are the agreed pilot date, technician availability and real team capacity?
- Provenance: the supplied change notes were inadvertently read in the initial file scan before planning commits existed. The baseline commits document a scenario baseline, not an unseen-change experiment. This ordering limitation cannot be repaired by rewriting history.
