---
id: "rtf-framework"
title: "RTF Framework: Role, Task, Format"
description: "Structure your prompt in 3 parts — define a Role, describe the Task, and specify the output Format."
category: "frameworks/basic"
tags: ["rtf", "framework", "role", "task", "format", "beginner"]
variables:
  - name: "role"
    label: "Role (what expert/persona should the AI be?)"
    required: true
  - name: "task"
    label: "Task (what do you need done?)"
    required: true
  - name: "output_format"
    label: "Output Format (e.g. bullet list, markdown table, JSON, paragraph)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

**Role:** You are {{role}}.

**Task:** {{task}}

**Format:** Provide your response in the following format: {{output_format}}
