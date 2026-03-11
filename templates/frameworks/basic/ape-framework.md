---
id: "ape-framework"
title: "APE Framework: Action, Purpose, Expectation"
description: "Generate an APE-structured prompt to delegate work to an AI agent — define Action, Purpose, and Expectation."
category: "frameworks/basic"
tags: ["ape", "framework", "prompt-generation", "delegation", "agent"]
variables:
  - name: "action"
    label: "Action (the specific thing you want the agent to do)"
    required: true
  - name: "purpose"
    label: "Purpose (why this matters — context that shapes quality)"
    required: true
  - name: "expectation"
    label: "Expectation (what the output must include or achieve)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a focused, ready-to-use prompt using the APE (Action, Purpose, Expectation) framework.

Apply the structure:
- **A — Action:** State "{{action}}" as an imperative — what the agent must do, starting now.
- **P — Purpose:** Contextualize with "{{purpose}}" — this shapes tone, depth, and priorities. The agent needs this to make good judgment calls.
- **E — Expectation:** Specify "{{expectation}}" precisely — what must be in the output, what quality standard it must meet, and what would make this unusable.

Output: the complete APE prompt only. Direct and dense — every word should earn its place. Ready to hand off to Claude, Cursor, or any AI agent.
