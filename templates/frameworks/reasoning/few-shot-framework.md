---
id: "few-shot-framework"
title: "Few-Shot: Example-Pattern Delegation Prompt"
description: "Generate a few-shot prompt that teaches an AI agent an exact input/output pattern through examples — then applies it to your actual input."
category: "frameworks/reasoning"
tags: ["few-shot", "examples", "pattern", "in-context-learning", "agent", "delegation"]
variables:
  - name: "task_description"
    label: "Task Description (what pattern/transformation should the agent learn?)"
    required: true
  - name: "example_input_1"
    label: "Example Input 1"
    required: true
  - name: "example_output_1"
    label: "Example Output 1"
    required: true
  - name: "example_input_2"
    label: "Example Input 2"
    required: true
  - name: "example_output_2"
    label: "Example Output 2"
    required: true
  - name: "actual_input"
    label: "Actual Input (what you want the agent to process)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a few-shot delegation prompt that teaches an AI agent the exact pattern through examples, then applies it.

Task: {{task_description}}

Structure the generated prompt as:
1. A one-sentence instruction establishing the agent's task
2. Example 1 — Input: {{example_input_1}} → Output: {{example_output_1}}
3. Example 2 — Input: {{example_input_2}} → Output: {{example_output_2}}
4. The actual task — Input: {{actual_input}} → Output: [agent completes this]

The generated prompt must:
- Present examples in identical format so the pattern is unambiguous
- Not explain the pattern — show it through examples and let the agent infer
- Include a brief instruction to match the format exactly, not improvise
- Be ready to paste directly into any AI agent that supports in-context learning

Output: the complete few-shot prompt only. Clean, structured, and immediately usable.
