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

- FR-1 [Must] The system shall require successful university sign-in before granting access to group content or student, officer, and moderation actions. [Source: UR-1, UR-5; release boundary]
- FR-2 [Must] The system shall let an authenticated student follow or unfollow a verified group and view its published announcements and events, subject to event-audience restrictions. [Source: UR-1]
- FR-3 [Must] The system shall let an authenticated student create or withdraw their own RSVP for a visible, uncancelled event, with a new RSVP's identity private by default and visible to other eligible attendees only after that student explicitly opts in; opting out shall remove that identity from attendee views. [Source: UR-2]
- FR-4 [Must] The system shall let approved officers of the same group create, save, open, and edit shared announcement and event drafts. [Source: UR-4]
- FR-5 [Must] The system shall let an approved officer publish a draft only for their own verified group and reject every other user's publishing attempt without publishing the draft. [Source: UR-5, UR-10]
- FR-6 [Must] The system shall let an approved officer select whole-university or members-only visibility for their group's event. [Source: UR-6]
- FR-7 [Must] The system shall deny a non-member access to a members-only event through the feed, search, a direct link, and an RSVP attempt. [Source: UR-6, UR-2]
- FR-8 [Must] The system shall create a change notification for every current RSVP when an approved officer saves a change to a published event's time or place. [Source: UR-7]
- FR-9 [Must] The system shall let an authenticated user report an announcement, event, or group profile with an item reference and non-empty reason, rejecting reports that omit either field. [Source: UR-8]
- FR-10 [Must] The system shall let an authorized moderator hide reported content from ordinary users while retaining the report, a snapshot of the reported content, and the decision record for authorized appeal review. [Source: UR-9]
- FR-11 [Must] The system shall record the deciding moderator's identity, action, affected item, reason, and timestamp for each hide, restore, or appeal decision. [Source: UR-9]
- FR-12 [Must] The system shall display the official badge only while the group's verification is approved by an authorized Student Affairs user, rejecting an ordinary officer's attempt to grant or revoke verification. [Source: UR-10]
- FR-13 [Must] The system shall delete all attendance records and attendance-identifying copies for a cancelled event no later than 30 days after the cancellation timestamp, including copies in exports, backups, and moderation evidence. [Source: UR-12]
- FR-14 [Must] The system shall show authorized moderators the item snapshot, reason, and report time for impersonation and repeated-announcement reports. [Source: UR-8]
- FR-15 [Must] The system shall let an approved officer appeal a moderation decision concerning their own group, link the appeal to that decision and its retained evidence, and deny access to another group's appeal. [Source: UR-9]
- FR-16 [Must] The system shall let an authorized moderator record an appeal outcome and reason, restoring content if the decision is reversed, and make the outcome visible to the appealing group's approved officers. [Source: UR-9]
- FR-17 [Must] The system shall let an approved officer correct or cancel their own group's published event and record the cancellation timestamp used by the attendance-deletion rule. [Source: UR-7, UR-12]
- FR-18 [Must] The system shall deny ordinary students and group officers access to private RSVP identities, while addressing event-change notifications to the RSVP owner without revealing the attendee list. [Source: UR-2, UR-13; A4]
- FR-19 [Must] The system shall collect no personal-data fields outside the approved purpose inventory in A5 and shall reject profile updates containing undeclared personal-data fields. [Source: UR-13]
- FR-20 [Could] The system shall let a moderator filter the report queue by reported item so all reports for that item can be reviewed together. [Source: UR-14]

## 4. Non-functional requirements

- NFR-1 [Must] The system shall support keyboard and screen-reader completion of the main student flows. [Measure: all six flows in A1 can be completed in Safari with VoiceOver and keyboard-only input without an unlabeled action, keyboard trap, or unannounced success/error result during release testing; record tested OS/browser versions] [Source: UR-3]
- NFR-2 [Should] The system shall respond promptly under the provisional pilot workload. [Measure: p95 end-to-end response time no more than 2 seconds and failed requests below 1% during a 10-minute run of 200 concurrent authenticated sessions, each issuing one request every 5 seconds using the request mix and dataset in A2] [Source: UR-11]
- NFR-3 [Must] The system shall support the main student flows on a narrow phone viewport. [Measure: all six A1 flows complete at 320 CSS pixels width with controls visible and operable and no horizontal page scrolling in the release browser test; assumed target A3] [Source: UR-3]
- NFR-4 [Must] The system shall support the pilot population. [Measure: all Must functional acceptance checks pass without missing or incorrectly attributed records on a dataset of 5,000 student accounts and 200 groups, with content and membership fixtures specified in A2] [Source: UR-11]
- NFR-5 [Must] The system shall meet the cancelled-event attendance-retention limit across all retained copies. [Measure: at cancellation time plus 30 days, a deletion test finds zero attendance records or attendance-identifying copies for that event in active storage, exports, backups, or moderation evidence; repeat after a supported restore procedure] [Source: UR-12]

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

### Assumptions

- A1: The accessibility test set is university sign-in, following/unfollowing, feed/event viewing, RSVP/withdrawal/privacy choice, reading a change notification, and reporting. Safari with VoiceOver plus keyboard-only testing is the proposed minimum release test setup, not a claim of compliance with an accessibility standard. S1 must confirm representative devices and assistive technologies.
- A2: Provisional load targets are 200 concurrent sessions, one request per session every 5 seconds for 10 minutes, p95 at most 2 seconds, and fewer than 1% failed requests. Fixtures contain 5,000 students, 200 groups, 1,000 published events, 1,000 announcements, five group memberships per student, and 20 RSVPs per event. The request mix is 50% feed reads, 30% event views, and 20% RSVP create/withdraw actions against eligible events. These workload and fixture numbers are team assumptions; only 5,000 students and 200 groups come from S4. Use a representative pilot deployment, document its resources and network conditions, and exclude third-party sign-in latency from this workload. NFR-2 is a provisional Should target pending Q1.
- A3: The 320 CSS pixel viewport is a proposed measurable minimum, not a number supplied by S1.
- A4: "Public" attendee visibility means visibility to other authenticated users who are eligible to view the event, never anonymous visitors. Private RSVP identities are hidden from ordinary attendees and officers; event notifications do not require exposing these identities. Necessary exceptional operational access requires a defined policy before launch (Q2).
- A5: Proposed personal-data inventory: university-issued account identifier (sign-in, ownership and authorization); university display name (officer attribution and explicit opt-in attendee display); group membership and officer approval (authorization); follow relationships (feed); event/RSVP identifier and visibility choice (RSVP and notifications); notification recipient/read state (private updates); and reporter/moderator/appellant identifier, reason and timestamp (reports and accountability). No phone number, home address, date of birth, payment data, or unrelated profile fields are requested. Do not store university passwords. S5 must approve field purposes, operational access, and retention; report text must not solicit unnecessary personal data.
- A6: The 30-day attendance deletion deadline is not extended by an appeal. Moderation evidence can retain reported content and decisions but must remove cancelled-event attendance identities by the same deadline. Backup/export procedures must make this verifiable. S3 and S5 must agree the separate retention period for other evidence; until then this is a release-blocking policy question, not permission to retain it indefinitely.
- A7: Grouping reports by item is an optional proposal derived from S3/S6, not an explicit stakeholder request. UR-14 and FR-20 are Could and cannot delay required moderation or abuse handling.

### Open questions

- Q1: S4, what is the Orientation Week date and expected peak concurrent use/request rate? Approve or replace A2 before committing to pilot capacity or a launch date. Population size alone does not establish traffic.
- Q2: S1/S2/S5, does any operational role need access to private RSVP identities, for what necessary purpose, and with which access/audit restrictions? Proposed default: officers cannot see them.
- Q3: S3/S5, what retention period and access rules apply to non-attendance moderation and appeal evidence? How must identifiers embedded in reports be redacted? Confirm before deployment.
- Q4: S4, which Student Affairs role grants/revokes verification, and which authority supplies and updates group membership and officer approval? Test fixtures assume these roles are explicitly assigned.
- Q5: S2, which notification channel and delivery deadline are acceptable for event corrections, and should cancellation also notify current RSVPs? Agree observable delivery behaviour before implementation.
- Q6: S3/S4, is manual report review and hiding sufficient for the pilot's repeated-post risk, or must automatic throttling and compromised-account recovery be included? Automated controls are not silently assumed to exist.

