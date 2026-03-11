---
id: "user-persona"
title: "User Persona Builder: Rich, Research-Grounded Profile"
description: "Create a detailed, research-grounded user persona with demographics, motivations, pain points, behaviors, and Jobs-to-Be-Done."
category: "fields/design"
tags: ["persona", "ux", "user-research", "design", "empathy", "product"]
variables:
  - name: "product"
    label: "Product or Service (what is the persona using?)"
    required: true
  - name: "user_segment"
    label: "User Segment (describe the type of user e.g. 'freelance designer aged 25-35')"
    required: true
  - name: "research_inputs"
    label: "Research Inputs (any data, quotes, or observations you have about this user)"
    required: false
  - name: "product_goal"
    label: "Product Goal (what do you want this persona to help you design for?)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are a senior UX researcher. Create a detailed, realistic user persona for the following.

**Product:** {{product}}
**User Segment:** {{user_segment}}
**Research Inputs:** {{research_inputs}}
**Design Goal:** {{product_goal}}

Build a persona with these sections:

## Identity
- Name, age, location (make it specific and real-feeling)
- Job title and work context
- Tech savviness (1-5 scale with description)
- Quote that captures their worldview

## Goals & Motivations
- Primary goal when using {{product}}
- Underlying emotional motivation (the "why behind the why")
- Secondary goals

## Pain Points & Frustrations
- Top 3 frustrations with existing solutions
- Specific moments of friction (use concrete scenarios)
- What they've tried and why it failed

## Behaviors & Habits
- How they currently solve this problem (workarounds)
- Channels and tools they trust
- Decision-making style: research-heavy vs. gut-driven

## Jobs to Be Done
- Functional JTBD: "When I [situation], I want to [motivation], so I can [outcome]"
- Emotional JTBD: how they want to feel
- Social JTBD: how they want to be perceived

## Design Implications
3 specific design decisions this persona should influence.
