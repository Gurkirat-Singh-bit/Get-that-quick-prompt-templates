---
id: "chain-of-thought"
title: "Chain of Thought: Step-by-Step Reasoning"
description: "Guide the AI to reason through a problem sequentially — thinking aloud at each step before reaching a conclusion."
category: "frameworks/reasoning"
tags: ["chain-of-thought", "cot", "reasoning", "step-by-step", "problem-solving", "analysis"]
variables:
  - name: "problem"
    label: "Problem (what needs to be solved or analyzed?)"
    required: true
  - name: "context"
    label: "Context (relevant background or constraints)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

**Problem:** {{problem}}

**Context:** {{context}}

Think through this problem step by step. Do not jump to a conclusion — reason through each component sequentially:

1. Break the problem down into its core elements.
2. Analyze each element one at a time.
3. Show your reasoning at every step — state what you know and what you are inferring.
4. Identify any assumptions you are making and flag them explicitly.
5. Arrive at a well-supported conclusion only after completing all prior steps.

Think out loud throughout. Only provide your final answer after the full reasoning chain is complete.
