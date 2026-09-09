# CampusPulse requirements

Name or team: Hamdan Alameri

Date: 9 September 2026

Status: working draft

Use the source IDs `S1` to `S6` from the lab handout. Keep every requirement
short enough to test and trace.

## 1. Release scope

### In scope

- University sign-in and verified university groups in a browser-based pilot.
- Group announcements and events, shared officer drafts, and approved-officer publishing.
- Following groups, viewing their published content, and RSVP with private-by-default identities.
- Whole-university and members-only event audiences; corrections and notifications to current RSVPs.
- Reports, moderation, official verification, decision records, and group appeals.
- Phone-browser and screen-reader access for a pilot of 5,000 students and 200 groups before Orientation Week.

### Out of scope

- X-1: Native mobile applications.
- X-2: Direct messages.
- X-3: External users.
- X-4: Payments.
- X-5: Video hosting.
- X-6: AI recommendations.

## 2. User requirements

- UR-1 [Must] Students can follow university groups and find their published announcements and events in one service. [Source: S1]
- UR-2 [Must] Students can RSVP without exposing their identity to other attendees unless they explicitly choose to share it. [Source: S1, S5]
- UR-3 [Must] Students, including screen-reader users, can complete the main student activities in a phone browser. [Source: S1]
- UR-4 [Must] Approved group officers can collaborate on their group's drafts. [Source: S2]
- UR-5 [Must] Group officers can rely on publishing being restricted to approved officers of the relevant group. [Source: S2]
- UR-6 [Must] Group officers can restrict an event to group members or make it available to the university community. [Source: S2]
- UR-7 [Must] Students who RSVP are told when their event's time or place changes. [Source: S2]
- UR-8 [Must] Moderators can review reported content and its reason, including impersonation and repeated-post reports. [Source: S3, S6]
- UR-9 [Must] Moderators can hide harmful content while preserving the evidence and accountable decision history needed for a group's appeal. [Source: S3]
- UR-10 [Must] Students can trust that an official badge means Student Affairs checked the group. [Source: S4, S6]
- UR-11 [Must] Student Affairs can launch a pilot for 5,000 students and 200 groups before Orientation Week. [Source: S4]
- UR-12 [Must] Students' cancelled-event attendance data is deleted within 30 days of cancellation. [Source: S5]
- UR-13 [Must] Students provide only the personal data needed for the service. [Source: S5]
- UR-14 [Could] Moderators can review repeated reports about the same item together to reduce duplicate investigation. [Source: S3, S6; proposed enhancement, A7]

## 3. Functional requirements

Write at least six observable system behaviours. Start each one with "The
system shall" and trace it to one or more user requirements.

Format: `FR-1 [Must] The system shall ... [Source: UR-1]`

- FR-1 [Must] The system shall
- FR-2 [Must] The system shall
- FR-3 [Must] The system shall
- FR-4 [Must] The system shall
- FR-5 [Must] The system shall
- FR-6 [Must] The system shall

## 4. Non-functional requirements

Write at least four measurable quality requirements. State what is measured,
the target, and the condition under which the target applies. If you introduce
a number that is not in the handout, record it as an assumption or open
question in Section 8.

Format: `NFR-1 [Must] The system shall ... [Measure: target and condition] [Source: UR-1]`

- NFR-1 [Must] The system shall
- NFR-2 [Must] The system shall
- NFR-3 [Should] The system shall
- NFR-4 [Must] The system shall

## 5. User stories and acceptance criteria

Write at least three stories from different stakeholder viewpoints. Each story
needs at least two acceptance criteria. Across the set, include a failure,
permission boundary, privacy rule, or other non-happy path.

### US-1 [Source: S?, UR-?]

As a <role>,

I want <capability>,

so that <benefit>.

Acceptance criteria:

-
-

### US-2 [Source: S?, UR-?]

As a <role>,

I want <capability>,

so that <benefit>.

Acceptance criteria:

-
-

### US-3 [Source: S?, UR-?]

As a <role>,

I want <capability>,

so that <benefit>.

Acceptance criteria:

-
-

## 6. MoSCoW summary

List requirement or story IDs in every category. The Won't category must state
what is excluded from this release.

- Must:
- Should:
- Could:
- Won't this release:

## 7. Traceability

Add at least four complete paths. Every row should connect evidence to a user
requirement, a system requirement, and a user story.

| Stakeholder need | User requirement | System requirement | User story |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## 8. Assumptions and open questions

Separate decisions your team has assumed from questions that still need an
answer.

### Assumptions

- A1:

### Open questions

- Q1:
