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

Generate a task delegation prompt for creating a richly detailed user persona.

The prompt is configured for the following inputs:
- Product: {{product}}
- User segment: {{user_segment}}
- Research inputs: {{research_inputs}}
- Product goal: {{product_goal}}

The generated prompt must instruct the AI agent to:

1. Act as a senior UX researcher creating a persona that will drive real design decisions
2. Build a persona that feels like a specific, real person — not a demographic average — with these sections fully developed:
   - **Identity**: name, age, location (specific and plausible), job title and work context, tech savviness on a 1–5 scale with description, and a quote that captures their worldview
   - **Goals & Motivations**: primary goal when using the product, the underlying emotional motivation (the "why behind the why"), and secondary goals
   - **Pain Points & Frustrations**: top 3 frustrations with existing solutions, with concrete scenarios illustrating each friction point, and what they have tried and why it failed
   - **Behaviors & Habits**: how they currently solve the problem (workarounds), channels and tools they trust, and their decision-making style (research-heavy vs. gut-driven)
   - **Jobs to Be Done**: functional JTBD ("When I [situation], I want to [motivation], so I can [outcome]"), emotional JTBD (how they want to feel), and social JTBD (how they want to be perceived)
   - **Design Implications**: exactly 3 specific design decisions this persona should directly influence
3. Ground the persona in the research inputs provided — do not invent contradicting details
4. Avoid stereotypes; every detail must be defensible from the inputs or clearly labeled as an inference

Output: the complete task delegation prompt only. Ready for Claude or any UX research agent.
