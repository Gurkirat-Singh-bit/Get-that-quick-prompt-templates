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

Generate a task delegation prompt for writing a complete set of user stories with acceptance criteria.

The prompt is configured for the following inputs:
- Feature: {{feature}}
- User type: {{user_type}}
- User goal: {{user_goal}}
- Context: {{context}}

The generated prompt must instruct the AI agent to:

1. Act as a senior product manager writing production-ready user stories
2. Write all stories strictly in the format: "As a [user], I want [specific action] so that [concrete benefit]"
3. For each story, produce acceptance criteria in Given/When/Then format covering:
   - The happy path (primary success scenario)
   - At least 2 edge cases (boundary conditions, unusual but valid inputs)
   - At least 1 error state (what happens when something goes wrong)
4. Append a Definition of Done checklist to every story covering: functional requirement met, error states handled and communicated to the user, mobile/responsive coverage if applicable, accessibility requirements (WCAG 2.1 AA), and analytics event tracked
5. Flag any stories that require a design clarification or engineering spike before they can be estimated — and explain specifically what needs to be resolved
6. Cover the full feature scope: main happy path, edge cases, and failure scenarios — no gaps

Output: the complete task delegation prompt only. Ready for Claude or any PM-capable agent.
