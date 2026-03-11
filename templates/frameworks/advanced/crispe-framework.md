---
id: "crispe-framework"
title: "CRISPE Framework: Capacity, Insight, Statement, Personality, Experiment"
description: "Generate a CRISPE-structured agent prompt — the most powerful framework for expert-level, multi-variant AI agent delegation."
category: "frameworks/advanced"
tags: ["crispe", "framework", "prompt-generation", "advanced", "expert", "agent"]
variables:
  - name: "capacity"
    label: "Capacity (what expert is this agent? e.g. 'Staff ML engineer at a fintech company')"
    required: true
  - name: "insight"
    label: "Insight (background context the agent must factor in)"
    required: true
  - name: "statement"
    label: "Statement (the exact task or question)"
    required: true
  - name: "personality"
    label: "Personality (tone and communication style, e.g. direct, Socratic, encouraging)"
    required: true
  - name: "experiment"
    label: "Experiment (ask for multiple approaches, variants, or alternative solutions)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a complete, expert-grade agent prompt using the CRISPE framework. This will be used as a system prompt or task instruction for Claude, Cursor, or a custom AI agent.

Build it as follows:
- **C — Capacity:** Open by defining the agent as "{{capacity}}" — be specific about expertise level, domain, and context (not just "senior engineer" but the type, stack, and perspective).
- **I — Insight:** Give the agent "{{insight}}" before any instruction — this is the knowledge it must internalize and operate from.
- **S — Statement:** State "{{statement}}" as an unambiguous task — the agent must know exactly what it is being asked to produce.
- **P — Personality:** Lock in "{{personality}}" as the agent's communication mode — affects how it explains, challenges, and presents.
- **E — Experiment:** Incorporate "{{experiment}}" — instruct the agent to produce multiple approaches, alternatives, or variations rather than just one answer.

Output: the complete CRISPE-structured system prompt only. Long enough to fully configure the agent, short enough that every line earns its place. Ready for Claude Projects, Cursor rules, or API system parameter.
