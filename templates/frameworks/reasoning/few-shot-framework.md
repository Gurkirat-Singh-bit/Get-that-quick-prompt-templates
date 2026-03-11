---
id: "few-shot-framework"
title: "Few-Shot Prompting: Example-Guided Generation"
description: "Provide 2 input/output examples to teach the AI the exact pattern, then apply it to your actual input."
category: "frameworks/reasoning"
tags: ["few-shot", "examples", "pattern", "in-context-learning", "reasoning", "generation"]
variables:
  - name: "task_description"
    label: "Task Description (what transformation or task should the AI learn?)"
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
    label: "Your Actual Input (apply the learned pattern to this)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

**Task:** {{task_description}}

**Example 1:**
Input: {{example_input_1}}
Output: {{example_output_1}}

---

**Example 2:**
Input: {{example_input_2}}
Output: {{example_output_2}}

---

Now apply the same pattern to the following:
Input: {{actual_input}}
Output:
