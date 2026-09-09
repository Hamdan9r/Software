# CampusPulse stakeholder analysis

Name or team: Hamdan Alameri

Date: 9 September 2026

Analysis uses the S1–S6 source notes in the Lab 3 handout and reviews the existing local draft. Quadrants reflect decision authority and interest, rather than the severity of a possible attack.

Stakeholder types: end user, operations, business, regulator, negative
stakeholder

Power-interest quadrants: key player, keep satisfied, keep informed,
minimal effort

## S1

-   Stakeholder: Student attendee
-   Stakeholder type: end user
-   Power-interest quadrant: keep informed
-   Main goal: Find university events and announcements in one place,
    follow groups, and RSVP easily from a phone.
-   Main concern: RSVP privacy and accessibility, especially for
    students who use screen readers.
-   How you would involve or monitor this stakeholder: Run usability and
    accessibility tests with students, collect pilot feedback, and
    confirm that RSVP visibility defaults match student expectations.

## S2

-   Stakeholder: Group officer
-   Stakeholder type: end user
-   Power-interest quadrant: key player
-   Main goal: Collaboratively prepare announcements and events, publish
    to the correct audience, and keep attendees informed of changes.
-   Main concern: Only approved officers must be able to publish, while
    multiple officers may need to work on the same draft.
-   How you would involve or monitor this stakeholder: Include approved
    officers in workflow and permission testing, review draft/publish
    behaviour with them, and test whole-university versus members-only
    audiences.

## S3

-   Stakeholder: Campus moderator
-   Stakeholder type: operations
-   Power-interest quadrant: key player
-   Main goal: Review reports, hide harmful events quickly, preserve
    evidence for appeals, and maintain accountability.
-   Main concern: Moderation actions must not destroy the evidence
    needed for an appeal, and every decision must identify who made it.
-   How you would involve or monitor this stakeholder: Review moderation
    workflows with moderators, test urgent hiding and appeal cases, and
    audit whether every decision retains evidence and actor information.

## S4

-   Stakeholder: Student Affairs
-   Stakeholder type: business
-   Power-interest quadrant: key player
-   Main goal: Launch a trustworthy pilot for 5,000 students and 200
    groups before Orientation Week.
-   Main concern: The official badge must only identify groups that
    Student Affairs has actually verified, and the release must be
    realistic for the pilot deadline.
-   How you would involve or monitor this stakeholder: Hold regular
    scope and readiness reviews, obtain approval of the verification
    process, and report pilot capacity and unresolved launch risks.

## S5

-   Stakeholder: Data Protection Officer
-   Stakeholder type: regulator
-   Power-interest quadrant: keep satisfied
-   Main goal: Ensure CampusPulse collects only necessary personal data
    and applies privacy and retention rules.
-   Main concern: RSVP lists must be private by default and attendance
    data for cancelled events must be deleted within 30 days.
-   How you would involve or monitor this stakeholder: Conduct a privacy
    review before release, confirm the data inventory and retention
    rules, and provide evidence from deletion and privacy tests.

## S6

-   Stakeholder: Abusive or compromised actors
-   Stakeholder type: negative stakeholder
-   Power-interest quadrant: keep informed (monitoring interpretation only)
-   Main goal: Misuse CampusPulse by impersonating verified groups,
    publishing phishing events, or repeatedly posting the same
    announcement.
-   Main concern: From the project perspective, these actors threaten
    trust, safety, and the meaning of verification.
-   How you would involve or monitor this stakeholder: These actors have high interest in misuse but no legitimate decision authority. The quadrant means monitoring their behaviour, not disclosing internal controls or inviting them to reviews. Do not involve
    malicious actors in decisions; instead monitor reports and
    suspicious publishing patterns and test abuse cases such as
    impersonation and repeated posts.

## Conflicts to resolve

### Conflict 1

-   Stakeholders: S1 and S2
-   What conflicts: S2 needs officers to communicate event changes to people who RSVP, while S1 does not want an RSVP to
    place their name on a public list unless they choose that.
-   Proposed decision or follow-up question: Keep RSVP identity private
    from the public by default. The service can deliver event-change notifications privately without showing attendee names to officers. Officer access to private RSVP identities is denied unless a necessary, approved purpose is agreed.
    Ask Student Affairs and the Data Protection Officer whether officers
    need to see attendee names at all, or whether notifications can work
    without exposing identities.

### Conflict 2

-   Stakeholders: S3 and S5
-   What conflicts: S3 needs evidence retained when content is hidden so
    that an appeal can be reviewed, while S5 requires unnecessary
    personal data to be removed and cancelled-event attendance data
    deleted within 30 days.
-   Proposed decision or follow-up question: Separate moderation
    evidence from attendance data. Apply the 30-day deletion rule to
    cancelled-event attendance data, and do not preserve attendance identities in evidence copies beyond that deadline. Keep the reported content and decision record needed for an appeal, with attendance identifiers removed. Ask the Data Protection
    Officer what retention period is permitted for moderation and appeal
    evidence.

### Conflict 3

-   Stakeholders: S4 and S6
-   What conflicts: S4 wants the official badge to prove that a group
    was checked, while S6 identifies impersonation of a verified group
    as an abuse case that could make a fake event appear trustworthy.
-   Proposed decision or follow-up question: Only Student
    Affairs-authorized verification may create or remove the official
    badge, and ordinary group officers cannot grant verification.
    Reports of impersonation must be reviewable by moderators.
