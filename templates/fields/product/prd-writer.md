---
id: "prd-writer"
title: "PRD Writer: Product Requirements Document"
description: "Generate a complete, structured Product Requirements Document — problem statement, goals, user stories, scope, metrics, and open questions."
category: "fields/product"
tags: ["prd", "product", "requirements", "roadmap", "user-stories", "product-manager"]
variables:
  - name: "feature_name"
    label: "Feature Name"
    required: true
  - name: "problem_statement"
    label: "Problem Statement (what user pain or business gap does this solve?)"
    required: true
  - name: "target_user"
    label: "Target User (who is this for?)"
    required: true
  - name: "business_goal"
    label: "Business Goal (what metric or outcome should improve?)"
    required: true
  - name: "proposed_solution"
    label: "Proposed Solution (high-level approach)"
    required: true
  - name: "out_of_scope"
    label: "Out of Scope (what will NOT be included)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for writing a complete Product Requirements Document.

The prompt is configured for the following inputs:
- Feature: {{feature_name}}
- Problem: {{problem_statement}}
- Target user: {{target_user}}
- Business goal: {{business_goal}}
- Proposed solution: {{proposed_solution}}
- Out of scope: {{out_of_scope}}

The generated prompt must instruct the AI agent to:

1. Act as a senior product manager at a technology company
2. Write a complete PRD that includes every one of the following sections — no section may be vague, skipped, or filled with placeholders:
   - **Problem Statement**: articulate the user pain and business gap, including the cost of not solving it
   - **Goals & Success Metrics**: primary goal tied to the business goal, 2-3 measurable KPIs with target values, and counter-metrics to watch
   - **User Stories**: 4-6 stories in "As a [user], I want [action] so that [outcome]" format, each with acceptance criteria
   - **Functional Requirements**: numbered list of exactly what the feature must do
   - **Non-Functional Requirements**: performance, security, accessibility, and scalability requirements
   - **Scope & Phasing**: what is in MVP vs. future phases, with explicit out-of-scope items
   - **Open Questions**: unresolved decisions needing input from engineering, design, or stakeholders
   - **Dependencies & Risks**: potential blockers and top 3 risks
3. Ground every section in the specific inputs provided — no generic filler
4. Make the PRD ready to hand directly to an engineering team without revision

Output: the complete task delegation prompt only. Ready to paste into Claude.
