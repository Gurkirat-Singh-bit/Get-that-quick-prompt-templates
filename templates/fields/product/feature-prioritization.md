---
id: "feature-prioritization"
title: "Feature Prioritization: Impact vs. Effort Scoring"
description: "Prioritize a feature backlog using multiple frameworks (RICE, ICE, MoSCoW) and produce a ranked, defensible roadmap recommendation."
category: "fields/product"
tags: ["prioritization", "roadmap", "rice", "ice", "moscow", "product", "backlog"]
variables:
  - name: "features"
    label: "Features to Prioritize (list them, one per line)"
    required: true
  - name: "business_goal"
    label: "Current Business Goal (e.g. grow revenue, reduce churn, increase activation)"
    required: true
  - name: "constraints"
    label: "Constraints (team size, time horizon, tech limitations)"
    required: true
  - name: "user_segment"
    label: "Primary User Segment (who are we optimizing for?)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for prioritizing a feature backlog.

The prompt is configured for the following inputs:
- Features to prioritize: {{features}}
- Business goal: {{business_goal}}
- Constraints: {{constraints}}
- Primary user segment: {{user_segment}}

The generated prompt must instruct the AI agent to:

1. Act as a senior product manager conducting a rigorous backlog prioritization
2. Score every feature using RICE: Reach (users affected per quarter), Impact (3=massive / 2=high / 1=medium / 0.5=low / 0.25=minimal), Confidence (100% / 80% / 50%), and Effort (person-weeks) — show the calculation for each
3. Classify every feature using MoSCoW: Must Have / Should Have / Could Have / Won't Have this cycle — with a one-sentence rationale for each classification
4. Produce a ranked table combining both frameworks
5. Recommend the top 3 features to build next with a full paragraph of justification for each, grounded in the business goal and constraints
6. Identify features that should be deferred and explain why
7. Call out any features that need more discovery or user research before they can be reliably prioritized — and describe what that discovery would look like

Output: the complete task delegation prompt only. Ready for Claude or any strategic AI agent.
