---
id: "roses-framework"
title: "ROSES Framework: Role, Objective, Scenario, Expected Solution, Steps"
description: "Generate a ROSES-structured agent prompt — the most organized framework for delegating structured problem-solving to AI agents."
category: "frameworks/advanced"
tags: ["roses", "framework", "prompt-generation", "structured", "problem-solving", "agent"]
variables:
  - name: "agent_role"
    label: "Agent Role (what expert persona)"
    required: true
  - name: "objective"
    label: "Objective (what needs to be accomplished)"
    required: true
  - name: "scenario"
    label: "Scenario (the specific situation or problem)"
    required: true
  - name: "expected_solution"
    label: "Expected Solution (what a good answer looks like)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a complete, delegation-ready prompt using the ROSES (Role, Objective, Scenario, Expected Solution, Steps) framework.

Build it as follows:
- **R — Role:** Assign the agent the identity of "{{agent_role}}" — specific expertise and operating perspective.
- **O — Objective:** Define "{{objective}}" as the mission — what the agent is ultimately trying to deliver.
- **S — Scenario:** Describe "{{scenario}}" in detail — the specific problem, constraints, and environment.
- **E — Expected Solution:** Show the agent what "{{expected_solution}}" looks like — the standard it must reach.
- **S — Steps:** Require the agent to work through the scenario in a numbered, explicit step-by-step sequence, explaining reasoning at each step.

Output: the complete ROSES prompt only. Formatted so the receiving agent fully understands the scenario before acting, knows what success looks like, and must show its work. Ready for Claude, Cursor, or API agents.
