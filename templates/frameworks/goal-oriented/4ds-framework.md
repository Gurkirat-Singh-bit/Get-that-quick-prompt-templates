---
id: "4ds-framework"
title: "4Ds Framework: Define, Delimit, Direct, Detail"
description: "Generate a 4Ds-structured agent prompt to delegate project scoping and planning — produces a complete breakdown from definition to execution steps."
category: "frameworks/goal-oriented"
tags: ["4ds", "framework", "scoping", "planning", "agent", "delegation", "project"]
variables:
  - name: "project"
    label: "Project or Task to Scope"
    required: true
  - name: "context"
    label: "Context (background, constraints, current state)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a 4Ds agent prompt for delegating project scoping and planning.

Configure it for:
- Project: {{project}}
- Context: {{context}}

The generated prompt must instruct the agent to work through all four Ds:
1. **Define:** Articulate exactly what success looks like. What is delivered and how is completion verified?
2. **Delimit:** Establish hard scope boundaries — what is in, what is explicitly out, what constraints apply
3. **Direct:** Recommend the strategic approach — methodology, sequencing rationale, key decisions
4. **Detail:** Produce a granular execution plan — ordered tasks, logical dependencies, clear ownership model

The agent must not skip any D, and must complete them in sequence (each builds on the prior).

Output: the complete 4Ds agent prompt only. The receiving agent should produce a full project breakdown with no ambiguity left. Ready for Claude, GPT, or any planning agent.
