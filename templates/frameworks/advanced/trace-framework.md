---
id: "trace-framework"
title: "TRACE Framework: Topic, Reason, Audience, Counterargument, Evidence"
description: "Generate a TRACE-structured prompt to delegate persuasive writing or argumentation to an AI agent — with built-in counterargument handling."
category: "frameworks/advanced"
tags: ["trace", "framework", "prompt-generation", "persuasion", "argumentation", "agent"]
variables:
  - name: "topic"
    label: "Topic (the claim or position to argue)"
    required: true
  - name: "reason"
    label: "Reason (why this position is correct or important)"
    required: true
  - name: "audience"
    label: "Audience (who needs to be persuaded)"
    required: true
  - name: "evidence"
    label: "Evidence (data, examples, or facts available to use)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a persuasion-focused agent prompt using the TRACE (Topic, Reason, Audience, Counterargument, Evidence) framework.

Build it as follows:
- **T — Topic:** Assign the agent the position: "{{topic}}" — stated as a clear, arguable claim.
- **R — Reason:** Give the agent "{{reason}}" — the core logic it must build its argument around.
- **A — Audience:** Define "{{audience}}" in detail — their biases, knowledge level, and what kind of argument moves them.
- **C — Counterargument:** Instruct the agent to proactively identify and address the 2-3 strongest opposing arguments before they are raised — this is non-negotiable.
- **E — Evidence:** Provide "{{evidence}}" and require the agent to anchor every major claim to this evidence.

Output: the complete TRACE agent prompt only. The prompt should force the agent to build a case that is both persuasive AND intellectually honest about opposition. Ready to hand to Claude, GPT, or any writing agent.
