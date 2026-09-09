# CampusPulse requirements

Name or team: Hamdan Alameri

Date: 9 September 2026

Status: reviewed specification; assumptions and stakeholder decisions remain open

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
- FR-8 [Must] The system shall make an event-change notice visible in the private notification list of every user with a current RSVP at the time an approved officer successfully saves a published event's time or place change, within 60 seconds of that save; the notice shall show the new time/place only to a user still authorized to view the event. [Source: UR-7; assumed delivery target A8]
- FR-9 [Must] The system shall let an authenticated user report an announcement, event, or group profile with an item reference and non-empty reason, rejecting reports that omit either field. [Source: UR-8]
- FR-10 [Must] The system shall let an authorized moderator hide reported content from ordinary users while retaining the report, a snapshot of the reported content, and the decision record for authorized appeal review. [Source: UR-9]
- FR-11 [Must] The system shall record the deciding moderator's identity, action, affected item, reason, and timestamp for each hide, restore, or appeal decision. [Source: UR-9]
- FR-12 [Must] The system shall display the official badge only while the group's verification is approved by an authorized Student Affairs user, rejecting an ordinary officer's attempt to grant or revoke verification. [Source: UR-10]
- FR-13 [Must] The system shall delete all attendance records and attendance-identifying copies for a cancelled event no later than 30 days after the cancellation timestamp, including service-managed exports, backups, and moderation evidence. [Source: UR-12]
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
- NFR-5 [Must] The system shall meet the cancelled-event attendance-retention limit across all retained copies. [Measure: at cancellation time plus 30 days, a deletion test finds zero attendance records or attendance-identifying copies for that event in active storage, service-managed exports, backups, or moderation evidence; repeat after a supported restore procedure] [Source: UR-12]

## 5. User stories and acceptance criteria

### US-1 [Source: S1, S5, UR-2]

As a student attendee, I want to control whether other attendees see my RSVP identity, so that attending does not disclose my interests without my choice.

Acceptance criteria:

- Given an eligible signed-in student, when they RSVP without changing visibility, then the RSVP is recorded and neither another attendee nor a group officer can see that identity.
- Given a private RSVP, when its owner opts in to visibility, then only authenticated users eligible to view the event can see the identity; after opting out it disappears from those views.
- Given an existing RSVP, when its owner withdraws it, then the student is no longer recorded as a current attendee.

### US-2 [Source: S2, UR-4, UR-5, UR-6]

As a group officer, I want to share drafts and publish to the correct audience, so that our group can collaborate without exposing restricted content.

Acceptance criteria:

- Given two approved officers of one verified group, when one saves a draft announcement or event, then the other can open, edit, and publish it.
- Given an ordinary student or an officer of a different group, when they attempt to publish that draft, then publication is rejected and the draft stays unpublished.
- Given a members-only event, when a non-member uses the feed, search, a direct link, or an RSVP action, then event content and RSVP access are denied; a member can view and RSVP.

### US-3 [Source: S2, UR-7]

As a student who RSVP'd, I want to receive time and place corrections, so that I can attend at the correct location and time.

Acceptance criteria:

- Given current RSVPs, when an approved officer successfully saves a time or place change to the published event, then a notice is visible in each current RSVP owner's private notification list within 60 seconds, showing the updated time/place to users still eligible to view the event.
- Given a failed or unauthorized update, when it is rejected, then no change notification is created and the published details remain unchanged.
- Given a current RSVP owner who is no longer authorized to view the event, when the correction notice is opened, then restricted event details are not shown.
- Given a student who withdrew their RSVP before the update, when the officer saves a correction, then that student receives no new correction notification.

### US-4 [Source: S3, S6, UR-8, UR-9]

As a campus moderator, I want to act on reports and review appeals with retained evidence, so that harmful content can be hidden and decisions remain accountable.

Acceptance criteria:

- Given a report of an event, announcement, or group profile with an item and reason, when a moderator opens it, then its content snapshot, reason, and report time are visible; missing-item or empty-reason reports are rejected.
- Given an authorized moderator, when they hide the reported item, then ordinary users cannot retrieve it through lists or direct links, while authorized moderators retain the evidence and an audit entry with actor, action, item, reason, and timestamp.
- Given a hidden item, when an approved officer of its group appeals, then the appeal links to the original decision and evidence; another group's officer cannot open it.
- Given an appeal, when an authorized moderator reverses the hide decision with a reason, then content is restored, the outcome is recorded, and the appealing group's officers can read it.

### US-5 [Source: S4, S6, UR-10]

As Student Affairs, I want to control official verification, so that a badge reliably distinguishes a checked group from an impersonator.

Acceptance criteria:

- Given an authorized Student Affairs user, when they approve verification, then the group's profile and published content display its official badge; revoking verification removes that badge.
- Given an ordinary group officer, when they attempt to grant verification, then the action is rejected and no official badge is granted.

### US-6 [Source: S4, UR-11]

As Student Affairs, I want evidence that the pilot handles the stated population, so that I can assess readiness before Orientation Week.

Acceptance criteria:

- Given the A2 dataset with 5,000 students and 200 groups, when all Must functional acceptance checks run, then every check passes without missing or misattributed records.
- Given a readiness review, when the NFR-2 load scenario runs on the documented pilot environment, then its p95 latency and error rate are reported against the provisional Should targets of 2 seconds and below 1%; a failure is recorded for a scope/performance decision and is not called a pass.
- Given no agreed Orientation Week date or peak-load figure, when readiness is assessed, then Q1 remains open and the population test alone is not treated as proof of peak readiness.

### US-7 [Source: S5, UR-12, UR-13]

As the Data Protection Officer, I want necessary data collection and timely deletion of cancelled-event attendance data, so that the pilot does not keep unrelated or expired personal information.

Acceptance criteria:

- Given a cancelled event with attendance copies in supported storage, service-managed exports, backups, and moderation evidence, when 30 days have elapsed, then no attendance records or attendance-identifying copies remain, including after a supported restore.
- Given an event that has not been cancelled, when its creation date reaches 30 days, then the cancellation-based deletion rule does not delete its attendance records.
- Given a profile update containing a phone-number field outside the A5 inventory, when it is submitted, then that field is rejected and is not stored.

### US-8 [Source: S1, UR-1, UR-3]

As a student using a phone and screen reader, I want an accessible group feed and event activities, so that I can participate without switching to another device or service.

Acceptance criteria:

- Given successful university sign-in, when a student follows a verified group, then its audience-eligible published announcements and events are available in the followed-group feed; unfollowing removes that group's contribution from that feed.
- Given the A1 accessibility setup, when each of its six flows is performed, then every flow completes without unlabeled actions, keyboard traps, or unannounced success/error results.
- Given a 320 CSS pixel viewport, when each A1 flow is performed, then controls remain visible and operable without horizontal page scrolling.
- Given unsuccessful university sign-in, when a user opens a content URL, then university-only content is not shown.

### US-9 [Source: S3, S6, UR-14]

As a moderator, I want reports grouped by item, so that I can avoid investigating the same content repeatedly. This is a Could enhancement.

Acceptance criteria:

- Given multiple reports about one item and reports about another, when the moderator filters by the first item, then only reports about that item are shown.
- Given that filtered view, when the moderator opens each report, then its individual reason and report time remain available.

## 6. MoSCoW summary

- Must: UR-1 through UR-13; FR-1 through FR-19; NFR-1, NFR-3, NFR-4, NFR-5; US-1 through US-8 (US-6's latency criterion explicitly evaluates a provisional Should target).
- Should: NFR-2, the provisional latency/error target under A2. Confirm peak demand before deciding whether a revised target must become a release gate.
- Could: UR-14, FR-20, US-9, grouping related reports. Core abuse-report handling remains Must.
- Won't this release: X-1 native mobile applications; X-2 direct messages; X-3 external users; X-4 payments; X-5 video hosting; X-6 AI recommendations. These IDs are the scope exclusions in Section 1.

## 7. Traceability

| Stakeholder need | User requirement | System requirement | User story |
|---|---|---|---|
| S1: one place for followed groups' updates | UR-1 | FR-1, FR-2 | US-8: sign-in and followed-group feed |
| S1/S5: private RSVP unless explicitly shared | UR-2 | FR-3, FR-18 | US-1: default privacy, opt-in/out, withdrawal |
| S1: phone and screen-reader access | UR-3 | NFR-1, NFR-3 | US-8: all six accessible phone flows |
| S2: officers share drafts | UR-4 | FR-4 | US-2: another officer finishes a draft |
| S2: only approved officers publish | UR-5 | FR-1, FR-5 | US-2: authorized and rejected publishing |
| S2: university or members-only events | UR-6 | FR-6, FR-7 | US-2: audience and direct-link boundary |
| S2: tell current RSVPs about a time/place correction | UR-7 | FR-8: private notice visible within 60 seconds, details subject to audience permission; FR-17 | US-3: visible correction notice, failed-update and access cases |
| S3/S6: reports show content and reason, including abuse | UR-8 | FR-9, FR-14 | US-4: report evidence and rejected incomplete report |
| S3: hide content, preserve evidence and decision actor, support appeals | UR-9 | FR-10, FR-11, FR-15, FR-16 | US-4: hide, group appeal boundary, recorded outcome |
| S4/S6: checked groups alone receive the official badge | UR-10 | FR-5, FR-12 | US-5: grant/revoke and unauthorized attempt |
| S4: pilot for 5,000 students and 200 groups | UR-11 | NFR-4; provisional NFR-2 | US-6: population test, measured latency, launch unknowns |
| S5: delete cancelled-event attendance within 30 days | UR-12 | FR-13, FR-17, NFR-5 | US-7: deletion across copies and non-cancelled boundary |
| S5: collect only needed personal data | UR-13 | FR-18, FR-19 | US-1: private identities; US-7: undeclared field rejection |
| S3/S6: reduce repeat investigation (A7 proposal) | UR-14 | FR-20 | US-9: filtered reports retain individual evidence |

## 8. Assumptions and open questions

### Assumptions

- A1: The accessibility test set is university sign-in, following/unfollowing, feed/event viewing, RSVP/withdrawal/privacy choice, reading a change notification, and reporting. Safari with VoiceOver plus keyboard-only testing is the proposed minimum release test setup, not a claim of compliance with an accessibility standard. S1 must confirm representative devices and assistive technologies.
- A2: Provisional load targets are 200 concurrent sessions, one request per session every 5 seconds for 10 minutes, p95 at most 2 seconds, and fewer than 1% failed requests. Fixtures contain 5,000 students, 200 groups, 1,000 published events, 1,000 announcements, five group memberships per student, and 20 RSVPs per event. The request mix is 50% feed reads, 30% event views, and 20% RSVP create/withdraw actions against eligible events. These workload and fixture numbers are team assumptions; only 5,000 students and 200 groups come from S4. Use a representative pilot deployment, document its resources and network conditions, and exclude third-party sign-in latency from this workload. NFR-2 is a provisional Should target pending Q1.
- A3: The 320 CSS pixel viewport is a proposed measurable minimum, not a number supplied by S1.
- A4: "Public" attendee visibility means visibility to other authenticated users who are eligible to view the event, never anonymous visitors. Private RSVP identities are hidden from ordinary attendees and officers; event notifications do not require exposing these identities. Necessary exceptional operational access requires a defined policy before launch (Q2).
- A5: Proposed personal-data inventory: university-issued account identifier (sign-in, ownership and authorization); university display name (officer attribution and explicit opt-in attendee display); group membership and officer approval (authorization); follow relationships (feed); event/RSVP identifier and visibility choice (RSVP and notifications); notification recipient/read state (private updates); and reporter/moderator/appellant identifier, reason and timestamp (reports and accountability). No phone number, home address, date of birth, payment data, or unrelated profile fields are requested. Do not store university passwords. S5 must approve field purposes, operational access, and retention; report text must not solicit unnecessary personal data.
- A6: The 30-day attendance deletion deadline is not extended by an appeal. Moderation evidence can retain reported content and decisions but must remove cancelled-event attendance identities by the same deadline. Service-managed backup/export procedures must make this verifiable; the service cannot erase independently saved copies outside its control and must avoid offering exports of private attendee identities. S3 and S5 must agree the separate retention period for other evidence; until then this is a release-blocking policy question, not permission to retain it indefinitely.
- A7: Grouping reports by item is an optional proposal derived from S3/S6, not an explicit stakeholder request. UR-14 and FR-20 are Could and cannot delay required moderation or abuse handling.
- A8: An in-service private notification list and a 60-second visibility deadline are proposed delivery behaviour for FR-8, not a channel or number supplied by S2. Q5 requires stakeholder confirmation. No direct-message feature is introduced. The notice must not bypass event-audience restrictions.

### Open questions

- Q1: S4, what is the Orientation Week date and expected peak concurrent use/request rate? Approve or replace A2 before committing to pilot capacity or a launch date. Population size alone does not establish traffic.
- Q2: S1/S2/S5, does any operational role need access to private RSVP identities, for what necessary purpose, and with which access/audit restrictions? Proposed default: officers cannot see them.
- Q3: S3/S5, what retention period and access rules apply to non-attendance moderation and appeal evidence? How must identifiers embedded in reports be redacted? Confirm before deployment.
- Q4: S4, which Student Affairs role grants/revokes verification, and which authority supplies and updates group membership and officer approval? Test fixtures assume these roles are explicitly assigned.
- Q5: S2, are a private in-service notification list and visibility within 60 seconds acceptable for event corrections (A8), or is another channel/deadline required? Should cancellation also notify current RSVPs? Confirm before implementation.
- Q6: S3/S4, is manual report review and hiding sufficient for the pilot's repeated-post risk, or must automatic throttling and compromised-account recovery be included? Automated controls are not silently assumed to exist.
