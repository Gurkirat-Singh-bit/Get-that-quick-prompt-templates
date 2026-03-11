---
id: "star-framework"
title: "STAR Framework: Situation, Task, Action, Result"
description: "Generate a STAR-structured prompt to delegate narrative, analysis, or problem-solving to an AI agent — grounded in Situation, Task, Action, Result."
category: "frameworks/basic"
tags: ["star", "framework", "prompt-generation", "delegation", "storytelling", "agent"]
variables:
  - name: "situation"
    label: "Situation (the context or background to establish)"
    required: true
  - name: "task"
    label: "Task (the challenge or objective within that situation)"
    required: true
  - name: "desired_result"
    label: "Desired Result (what the agent's output should achieve)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a ready-to-use prompt using the STAR (Situation, Task, Action, Result) framework.

Apply the structure:
- **S — Situation:** Establish "{{situation}}" as rich context — the agent needs this to frame everything correctly.
- **T — Task:** Define "{{task}}" as the specific challenge within that situation.
- **A — Action:** Instruct the agent to reason through and describe the best action(s) to take — step by step, with explicit reasoning.
- **R — Result:** Anchor to "{{desired_result}}" — the agent must ensure everything it produces drives toward this outcome.

Output: the complete STAR prompt only. Structured to give an AI agent full context before asking anything. Ready to paste into Claude, ChatGPT, or Cursor and immediately get a high-quality response.
