---
id: "creo-framework"
title: "CREO Framework: Context, Role, Evidence, Output"
description: "Generate a CREO-structured prompt to delegate evidence-grounded tasks to AI agents — ensures responses are factual, not hallucinated."
category: "frameworks/structured"
tags: ["creo", "framework", "prompt-generation", "evidence-based", "factual", "agent"]
variables:
  - name: "context"
    label: "Context (the situation or topic area)"
    required: true
  - name: "agent_role"
    label: "Agent Role (expert persona to adopt)"
    required: true
  - name: "evidence"
    label: "Evidence (data, facts, or source material the agent must use)"
    required: true
  - name: "output_format"
    label: "Output Format (how the response must be structured)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a ready-to-use prompt using the CREO (Context, Role, Evidence, Output) framework. This is specifically designed to produce factual, evidence-grounded responses from AI agents.

Build it as follows:
- **C — Context:** Establish "{{context}}" — the agent knows exactly what domain and situation it is operating in.
- **R — Role:** Assign the agent the persona of "{{agent_role}}" — this activates domain expertise and appropriate judgment.
- **E — Evidence:** Feed the agent "{{evidence}}" as the only ground truth — explicitly instruct it to stay within this evidence and flag if anything cannot be substantiated.
- **O — Output:** Define "{{output_format}}" strictly — structure, sections, length, and what to include vs. omit.

Output: the complete CREO prompt only. Include an explicit instruction: "Do not go beyond the provided evidence. If a claim cannot be supported, say so." Ready to paste into any AI agent.
