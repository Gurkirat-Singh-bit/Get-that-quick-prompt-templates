---
id: "crispe-framework"
title: "CRISPE Framework: Capacity, Insight, Statement, Personality, Experiment"
description: "An advanced 5-part framework originally from OpenAI — define the AI's Capacity/Role, provide Insight, state the task, set a Personality, and prompt Experimentation."
category: "frameworks/advanced"
tags: ["crispe", "framework", "capacity", "insight", "statement", "personality", "experiment", "advanced"]
variables:
  - name: "capacity"
    label: "Capacity/Role (what expert is the AI? e.g. senior developer, UX researcher)"
    required: true
  - name: "insight"
    label: "Insight (background info, data, or context the AI should factor in)"
    required: true
  - name: "statement"
    label: "Statement (the exact task or request)"
    required: true
  - name: "personality"
    label: "Personality (tone and communication style, e.g. direct, empathetic, Socratic)"
    required: true
  - name: "experiment"
    label: "Experiment (ask for multiple options, variations, or alternative approaches)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

**Capacity:** You are {{capacity}}.

**Insight:** Here is the relevant background you need to factor into your response: {{insight}}

**Statement:** Your task is to: {{statement}}

**Personality:** Communicate in a {{personality}} manner throughout your entire response.

**Experiment:** {{experiment}}

Draw on your capacity and the provided insight to complete the stated task. Maintain the defined personality consistently, and where prompted, provide multiple experimental approaches or variations.
