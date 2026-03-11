---
id: "risen-framework"
title: "RISEN Framework: Role, Instructions, Steps, End Goal, Narrowing"
description: "Generate a RISEN-structured prompt — the most precise framework for delegating complex, multi-step tasks to AI agents."
category: "frameworks/structured"
tags: ["risen", "framework", "prompt-generation", "delegation", "complex-tasks", "agent"]
variables:
  - name: "agent_role"
    label: "Agent Role (what expert persona should handle this?)"
    required: true
  - name: "task"
    label: "Task (what needs to be done?)"
    required: true
  - name: "end_goal"
    label: "End Goal (final deliverable or outcome)"
    required: true
  - name: "constraints"
    label: "Constraints (scope limits, format rules, tone, things to avoid)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a complete, production-ready prompt using the RISEN framework. This will be handed to an AI agent to execute.

Build it as follows:
- **R — Role:** Establish the agent as "{{agent_role}}" with the specific expertise needed for this task.
- **I — Instructions:** Translate "{{task}}" into clear, unambiguous instructions. No vagueness. No assumptions.
- **S — Steps:** Break the task into an explicit numbered sequence the agent must follow — each step should produce a checkable output.
- **E — End Goal:** Define "{{end_goal}}" precisely — the agent must know what done looks like before it starts.
- **N — Narrowing:** Enforce "{{constraints}}" as hard rules — scope, format, tone, what to skip, what to never do.

Output: the complete RISEN prompt only. Structured so an AI agent in Claude, Cursor, or any orchestration framework can execute it without follow-up clarification.
