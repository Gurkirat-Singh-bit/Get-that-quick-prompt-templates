---
id: "care-framework"
title: "CARE Framework: Context, Action, Result, Example"
description: "Generate a CARE-structured prompt for high-precision AI agent delegation — grounded in Context, Action, Result, and a guiding Example."
category: "frameworks/structured"
tags: ["care", "framework", "prompt-generation", "precision", "example-driven", "agent"]
variables:
  - name: "context"
    label: "Context (situation or background the agent needs to know)"
    required: true
  - name: "action"
    label: "Action (what the agent must do)"
    required: true
  - name: "result"
    label: "Result (what the output should achieve)"
    required: true
  - name: "example"
    label: "Example (a sample, reference, or prior work to model the output after)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a high-precision prompt using the CARE (Context, Action, Result, Example) framework. The output will be used as a task prompt for an AI agent.

Build it as follows:
- **C — Context:** Ground the agent with "{{context}}" — situational awareness before any instruction. This prevents misinterpretation.
- **A — Action:** Instruct the agent to perform "{{action}}" — written as an unambiguous directive.
- **R — Result:** Define "{{result}}" as the quality bar — what the output must accomplish and how it will be evaluated.
- **E — Example:** If available, use "{{example}}" as a reference — tell the agent to match the format, tone, or approach shown.

Output: the complete CARE prompt only. The example section should show the agent exactly what success looks like so it doesn't have to guess. Ready to paste into any AI agent.
