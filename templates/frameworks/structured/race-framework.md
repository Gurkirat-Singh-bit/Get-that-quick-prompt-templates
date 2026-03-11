---
id: "race-framework"
title: "RACE Framework: Role, Action, Context, Expectation"
description: "Generate a RACE-structured prompt to delegate role-based tasks to AI agents with full context and clear expectations."
category: "frameworks/structured"
tags: ["race", "framework", "prompt-generation", "delegation", "context", "agent"]
variables:
  - name: "role"
    label: "Role (what expert is the AI agent in this scenario?)"
    required: true
  - name: "action"
    label: "Action (what should the agent do?)"
    required: true
  - name: "context"
    label: "Context (relevant background the agent needs)"
    required: true
  - name: "expectation"
    label: "Expectation (what must the output include or achieve?)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a ready-to-use prompt using the RACE (Role, Action, Context, Expectation) framework. This prompt will be given directly to an AI agent.

Build it as follows:
- **R — Role:** Open by assigning the agent the identity of "{{role}}" — activate the right domain knowledge and voice.
- **A — Action:** State "{{action}}" as the agent's directive — specific, imperative, no ambiguity.
- **C — Context:** Feed the agent "{{context}}" before asking anything — the agent needs this to make good judgment calls.
- **E — Expectation:** Define "{{expectation}}" explicitly — what must appear in the output, what standard it must hit, and what would make it a failure.

Output: the complete RACE prompt only. Write it so a fresh AI agent with no prior context could read it once and execute perfectly. Ready for Claude, Cursor, GPT, or any AI.
