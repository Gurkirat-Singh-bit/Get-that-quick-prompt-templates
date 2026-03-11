---
id: "rtf-framework"
title: "RTF Framework: Role, Task, Format"
description: "Generate a clean RTF-structured prompt to delegate any task to an AI agent — define Role, Task, and output Format."
category: "frameworks/basic"
tags: ["rtf", "framework", "prompt-generation", "delegation", "agent"]
variables:
  - name: "role"
    label: "Role (what expert should the AI agent be?)"
    required: true
  - name: "task"
    label: "Task (what exactly do you want the agent to do?)"
    required: true
  - name: "output_format"
    label: "Output Format (e.g. markdown report, bullet list, JSON, numbered steps)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a clean, ready-to-use prompt using the RTF (Role, Task, Format) framework.

Apply the structure as follows:
- **R — Role:** Open by establishing the AI as "{{role}}" with specific expertise. One sentence that activates the right knowledge domain.
- **T — Task:** State "{{task}}" with full specificity — include constraints, context, and what a good result looks like.
- **F — Format:** Require output strictly in "{{output_format}}" — define the structure, length, and any sections needed.

Output: the complete RTF-structured prompt only. No explanation, no preamble. Start directly with the Role line. Make it tight, specific, and immediately usable in Claude, Cursor, or any AI.
