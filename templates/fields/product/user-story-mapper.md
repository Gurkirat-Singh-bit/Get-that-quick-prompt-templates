---
id: "user-story-mapper"
title: "User Story Mapper: Stories with Acceptance Criteria"
description: "Generate detailed user stories with INVEST-compliant acceptance criteria and edge cases for any feature."
category: "fields/product"
tags: ["user-story", "acceptance-criteria", "agile", "scrum", "product", "requirements"]
variables:
  - name: "feature"
    label: "Feature or Capability (what are you building?)"
    required: true
  - name: "user_type"
    label: "Primary User Type (e.g. free user, admin, guest)"
    required: true
  - name: "user_goal"
    label: "User Goal (what the user is trying to accomplish)"
    required: true
  - name: "context"
    label: "Context (product area, constraints, or existing system behavior)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are a senior product manager. Generate a complete set of user stories for the following feature.

**Feature:** {{feature}}
**Primary User:** {{user_type}}
**User Goal:** {{user_goal}}
**Context:** {{context}}

For each user story:

**Story:** As a {{user_type}}, I want to [specific action] so that [concrete benefit].

**Acceptance Criteria (Given/When/Then):**
- Given [precondition], When [action], Then [expected result]
- (include at least 3 scenarios per story: happy path, edge case, error state)

**Definition of Done:**
- [ ] Functional requirement met
- [ ] Error states handled and communicated to user
- [ ] Mobile/responsive if applicable
- [ ] Accessibility requirements met (WCAG 2.1 AA)
- [ ] Analytics event tracked

Generate stories for: the main happy path, at least 2 edge cases, and at least 1 error/failure scenario. Flag any stories that require design clarification or engineering spike before estimating.
