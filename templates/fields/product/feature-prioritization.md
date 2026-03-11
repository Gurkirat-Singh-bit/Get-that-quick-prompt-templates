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

You are a senior product manager. Prioritize the following feature backlog against the business goal.

**Business Goal:** {{business_goal}}
**Primary User:** {{user_segment}}
**Constraints:** {{constraints}}

**Features to prioritize:**
{{features}}

Score each feature using two frameworks:

**RICE Score** (Reach × Impact × Confidence ÷ Effort):
- Reach: users affected per quarter (estimate)
- Impact: effect on goal (3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal)
- Confidence: certainty in estimates (100%/80%/50%)
- Effort: person-weeks

**MoSCoW Classification:**
- Must Have / Should Have / Could Have / Won't Have (this cycle)

Produce:
1. A scored table with RICE ranking
2. Your top 3 recommended features to build next, with a one-paragraph justification for each
3. Features you recommend deferring and why
4. Any features that need more discovery before they can be prioritized
