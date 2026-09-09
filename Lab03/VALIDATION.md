# CampusPulse requirements review

Name or team: Hamdan Alameri

Reviewer: Codex-assisted document review against the Lab 3 handout and existing local draft; no stakeholder approval is claimed.

Date: 9 September 2026

## Validity

Do the requirements represent what the stakeholders need? Which IDs did you check, and what evidence supports them?

Response:

S1/S5 explicitly require RSVP privacy: UR-2, FR-3, FR-18 and US-1 cover the private default, opt-in, opt-out and officer boundary. S2 supports shared drafting (UR-4/FR-4), controlled publication (UR-5/FR-5), audience choice (UR-6/FR-6/FR-7), and corrections (UR-7/FR-8/US-3). S3 supports UR-8/UR-9 and FR-9–FR-16's reports, evidence, decisions and appeal path. S4 supports verification (UR-10/FR-12) and the population in UR-11/NFR-4. S5 directly supports FR-13's 30-day rule. S6 is addressed by mandatory report handling, verified publishing and moderator hiding; optional grouping in FR-20 is labeled a proposal in A7. Numerical assumptions and open policy decisions are not stakeholder facts.

## Consistency

Do any requirements contradict one another or the release scope?

Response:

X-1–X-6 are identical in scope and the Won't list. Phone-browser requirements NFR-1/NFR-3 do not introduce a native app. A8's notification list does not introduce direct messaging. FR-7's audience restriction also applies to FR-8 notification details and FR-3 attendee visibility. The S3/S5 retention conflict is resolved by FR-13, NFR-5 and A6: an appeal does not permit retaining cancelled-event attendance identities past 30 days; reported content and decision records can survive with those identifiers removed. Q3 still requires an approved retention period for other evidence. Could FR-20 does not weaken Must FR-14's abuse handling. NFR-2 is a provisional Should target; US-6 reports a failure honestly instead of declaring every such failure a passed release gate.

## Completeness

Is an important actor, normal flow, failure, permission, privacy rule, or boundary missing?

Response:

All S1–S6 actors and evidence are represented. FR-1/FR-2 and US-8 cover sign-in, following and viewing. FR-3 adds both RSVP and withdrawal, rather than only a privacy setting. FR-4/FR-5 cover collaborative drafting and publication. FR-6/FR-7/US-2 include denied direct-link and RSVP attempts. FR-9–FR-16/US-4 cover incomplete reports, hiding, evidence, group-authorized appeal, outcome and restoration. FR-17 supplies the cancellation timestamp that the deletion rule needs. FR-18/FR-19 cover private identity access and data minimization. US-6 now actually tests pilot capacity; the existing draft's capacity-to-badge-story link was removed. Q1–Q6 identify the remaining stakeholder questions about peak traffic/date, identity access, evidence retention, authority provisioning, notification expectations, and automated abuse controls. These cannot be resolved by claiming the document has stakeholder sign-off.

## Realism

Can the proposed release and its quality targets reasonably be delivered? Mark unsupported targets as assumptions or open questions.

Response:

This is a specification exercise, not an implemented or load-tested product. No runtime test result or stakeholder approval is claimed. The release excludes all six capabilities outside the brief. The 5,000 students/200 groups are supplied by S4; concurrency, latency, fixture sizes, request mix and test duration are A2 assumptions. Accessibility test conditions, viewport width and notification timing are A1/A3/A8 assumptions. Actual Orientation Week timing and peak demand are unknown (Q1), so neither launch feasibility nor peak capacity can yet be guaranteed. FR-13/NFR-5 intentionally include service-managed backups and exports; A6 clarifies the boundary of copies outside service control. Data inventory and evidence-retention policies require S5 approval before deployment. Could grouping can be dropped without removing core moderation.

## Verifiability

Could a tester decide whether each requirement passes or fails? Identify any wording that is still vague.

Response:

FR-5 has authorized/unauthorized publication outcomes, FR-7 has four denied access paths, and FR-9 rejects reports missing an item or reason. NFR-1 specifies six flows and observable accessibility failures; NFR-2 states the percentile, threshold, duration, concurrency, rate and request mix; NFR-3 specifies width and scrolling behaviour; NFR-4 gives population and functional pass criteria; NFR-5 defines the deadline, records, storage boundary and restore check. These are planned acceptance tests, not tests already executed. The initial FR-8 only required creating a notification record; that could pass even if an attendee never had an interface to read it. The revision specifies visibility, recipients, deadline and the audience boundary. Stakeholder-dependent terms such as the approved role roster and data inventory are tied to A4/A5 and Q2/Q4; those decisions remain required before implementation acceptance. Performance evidence must record environment details as required by A2.

## One requirement you revised

- Requirement ID: FR-8.
- Before: FR-8 [Must] The system shall create a change notification for every current RSVP when an approved officer saves a change to a published event's time or place. [Source: UR-7]
- What was wrong or missing: Creating a notification record did not guarantee the RSVP owner could see it. The delivery surface, deadline and behaviour after an audience-permission change were unspecified.
- After: FR-8 [Must] The system shall make an event-change notice visible in the private notification list of every user with a current RSVP at the time an approved officer successfully saves a published event's time or place change, within 60 seconds of that save; the notice shall show the new time/place only to a user still authorized to view the event. [Source: UR-7; assumed delivery target A8]
- Evidence or stakeholder to confirm the change: S2 says to tell people who RSVP'd if the place or time changes. S2 must confirm the proposed channel/deadline in A8/Q5. FR-7 and S2's members-only audience support the access boundary. The same revision is present in FR-8, US-3 acceptance criteria and the S2 → UR-7 → FR-8 → US-3 traceability row.

## Final check

- [x] Stakeholder conflicts have a decision or a follow-up question.
- [x] Scope exclusions agree with the Won't list.
- [x] Every FR and NFR traces to a user requirement.
- [x] Every NFR contains a measurable target and condition.
- [x] Traceability rows use IDs that exist in the document.
- [x] The revised requirement has also been updated in the traceability table.
