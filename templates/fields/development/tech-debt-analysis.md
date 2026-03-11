---
id: "tech-debt-analysis"
title: "Tech Debt Analysis: Identify, Categorize, Prioritize"
description: "Systematically identify and prioritize technical debt in a codebase — distinguish quick wins from strategic rewrites."
category: "fields/development"
tags: ["tech-debt", "architecture", "refactor", "engineering", "planning", "development"]
variables:
  - name: "codebase_description"
    label: "Codebase Description (what does the system do, rough size, age)"
    required: true
  - name: "pain_points"
    label: "Known Pain Points (areas that are slow to change, often break, or confuse developers)"
    required: true
  - name: "team_size"
    label: "Team Size and Velocity (e.g. 3 devs, shipping weekly)"
    required: false
  - name: "business_context"
    label: "Business Context (growth phase, upcoming launches, constraints)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are a senior engineering lead. Analyze the technical debt situation described below and produce a structured remediation plan.

**Codebase:** {{codebase_description}}

**Known Pain Points:** {{pain_points}}

**Team Context:** {{team_size}}

**Business Context:** {{business_context}}

Produce a tech debt report with the following sections:

**1. Debt Inventory**
Categorize each pain point into:
- **Deliberate debt** (shortcuts taken knowingly)
- **Accidental debt** (poor decisions made unknowingly)
- **Bit rot** (code that was fine but aged poorly)

**2. Impact Assessment**
For each debt item, score:
- Developer velocity impact (1-5)
- Risk of production incidents (1-5)
- Onboarding friction (1-5)

**3. Prioritization Matrix**
Classify each item as:
- **Quick win** — low effort, high impact, do first
- **Strategic investment** — high effort, high value, plan and schedule
- **Accept and document** — low priority, acknowledge and move on

**4. 90-Day Remediation Plan**
A concrete, phased plan that balances debt reduction with feature delivery. Include what to tackle in weeks 1-4, 5-8, and 9-12.
