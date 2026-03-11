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

You are a senior product manager at a technology company. Write a complete PRD for the following feature.

**Feature:** {{feature_name}}
**Target User:** {{target_user}}
**Problem:** {{problem_statement}}
**Business Goal:** {{business_goal}}
**Proposed Solution:** {{proposed_solution}}
**Out of Scope:** {{out_of_scope}}

Structure the PRD as follows:

## 1. Problem Statement
Articulate the user pain and business gap this feature addresses. Include the cost of not solving it.

## 2. Goals & Success Metrics
- Primary goal (tied to {{business_goal}})
- 2-3 measurable KPIs with target values
- Counter-metrics to watch (what should NOT get worse)

## 3. User Stories
Write 4-6 user stories in the format: "As a [user], I want to [action] so that [outcome]."
Include acceptance criteria for each.

## 4. Functional Requirements
Numbered list of exactly what the feature must do.

## 5. Non-Functional Requirements
Performance, security, accessibility, and scalability requirements.

## 6. Scope & Phasing
What is in MVP vs. future phases. Be explicit about what is out of scope.

## 7. Open Questions
List unresolved decisions that need input from engineering, design, or stakeholders.

## 8. Dependencies & Risks
What could block or delay this? What are the top 3 risks?
