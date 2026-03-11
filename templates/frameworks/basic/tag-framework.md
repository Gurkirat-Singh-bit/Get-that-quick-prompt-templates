---
id: "tag-framework"
title: "TAG Framework: Task, Action, Goal"
description: "Generate a TAG-structured prompt to delegate a focused task to an AI agent — specify Task, Action, and Goal."
category: "frameworks/basic"
tags: ["tag", "framework", "prompt-generation", "delegation", "agent"]
variables:
  - name: "task"
    label: "Task (what needs to be accomplished?)"
    required: true
  - name: "action"
    label: "Action (the specific approach or steps the agent should take)"
    required: true
  - name: "goal"
    label: "Goal (what does success look like?)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a concise, ready-to-use prompt using the TAG (Task, Action, Goal) framework.

Apply the structure:
- **T — Task:** Frame "{{task}}" as a clear, scoped directive the agent can act on immediately.
- **A — Action:** Translate "{{action}}" into specific, unambiguous steps the agent must take — no room for interpretation.
- **G — Goal:** Define "{{goal}}" as a measurable or observable outcome so the agent knows when it is done.

Output: the complete TAG prompt only. No meta-commentary. Write it so the agent receiving this prompt needs zero follow-up to begin. Ready to paste into Claude, GPT, or Cursor.
