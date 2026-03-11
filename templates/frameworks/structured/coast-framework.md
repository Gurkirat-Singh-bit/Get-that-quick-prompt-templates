---
id: "coast-framework"
title: "COAST Framework: Context, Objective, Actions, Scenario, Task"
description: "Generate a COAST-structured prompt to delegate strategic, scenario-based work to an AI agent with full situational framing."
category: "frameworks/structured"
tags: ["coast", "framework", "prompt-generation", "strategic", "scenario", "agent"]
variables:
  - name: "context"
    label: "Context (background situation)"
    required: true
  - name: "objective"
    label: "Objective (what the agent is ultimately trying to achieve)"
    required: true
  - name: "scenario"
    label: "Scenario (specific environment, constraints, or conditions)"
    required: true
  - name: "task"
    label: "Task (the exact action to execute)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a complete, delegation-ready prompt using the COAST (Context, Objective, Actions, Scenario, Task) framework.

Build it as follows:
- **C — Context:** Set up "{{context}}" — the agent reads this first to understand the world it is operating in.
- **O — Objective:** State "{{objective}}" clearly — this is the north star the agent keeps in view throughout.
- **A — Actions:** Instruct the agent to determine and sequence the best actions to reach the objective within the scenario — make this explicit.
- **S — Scenario:** Describe "{{scenario}}" as the specific operating environment — constraints, available resources, and conditions apply here.
- **T — Task:** Define "{{task}}" as the precise deliverable — what the agent produces and hands back.

Output: the complete COAST prompt only. Structured so the agent always knows its objective, its environment, and exactly what to produce. Ready for Claude, Cursor, or API agents.
