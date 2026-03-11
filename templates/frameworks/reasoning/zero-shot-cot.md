---
id: "zero-shot-cot"
title: "Zero-Shot Chain of Thought"
description: "Generate a zero-shot CoT prompt that triggers step-by-step reasoning in any AI agent without providing examples."
category: "frameworks/reasoning"
tags: ["zero-shot", "chain-of-thought", "cot", "reasoning", "agent", "no-examples"]
variables:
  - name: "task"
    label: "Task or Problem (what should the agent reason through?)"
    required: true
  - name: "agent_role"
    label: "Agent Role (what expert perspective to reason from)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a zero-shot Chain of Thought prompt for the following task. This prompt will be handed directly to an AI agent to trigger visible, step-by-step reasoning.

Task to reason through: {{task}}
Agent role: {{agent_role}}

The generated prompt must:
1. Establish the agent's role (if provided)
2. State the task clearly and completely
3. End with the trigger phrase: "Let's think step by step."
4. Include a format instruction: numbered steps, final answer clearly labeled

Keep it minimal — zero-shot CoT works because of its simplicity. The reasoning is triggered by the phrase, not by elaborate setup. The prompt should be under 100 words.

Output: the complete zero-shot CoT prompt only. Compact, direct, ready to paste into Claude, GPT, or Cursor.
