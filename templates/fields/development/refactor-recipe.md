---
id: "refactor-recipe"
title: "Refactor Agent: Task Delegation Prompt"
description: "Generate a task prompt to delegate a structured refactor to an AI coding agent — with clear goals, constraints, and a verify-behavior requirement."
category: "fields/development"
tags: ["refactor", "clean-code", "agent", "delegation", "cursor", "claude"]
variables:
  - name: "language"
    label: "Language / Framework"
    required: true
  - name: "refactor_goal"
    label: "Refactor Goal (e.g. extract functions, apply SOLID, reduce duplication, improve naming)"
    required: true
  - name: "must_preserve"
    label: "Must Preserve (behavior, interfaces, or APIs that cannot change)"
    required: true
  - name: "style_guide"
    label: "Style Guide or Conventions (what patterns to introduce or enforce)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a refactoring task prompt to delegate to an AI coding agent (Claude, Cursor, or similar).

Configure it for:
- Language: {{language}}
- Goal: {{refactor_goal}}
- Must not change: {{must_preserve}}
- Style guide: {{style_guide}}

The generated prompt must instruct the agent to:
1. First analyze the current code — describe the problems before touching anything
2. List the specific refactoring steps it will take — get implicit approval before writing
3. Implement the refactor, applying {{style_guide}} conventions throughout
4. For each significant change: explain why it is an improvement
5. Explicitly confirm that {{must_preserve}} is unchanged — state what tests or reasoning verify this
6. Call out any additional refactor opportunities noticed but left out of scope

Hard rule to include: Do not over-refactor. Only make changes needed for {{refactor_goal}}. If something wasn't asked for, mention it but don't change it.

Output: the complete refactor task prompt only. Ready to paste into Cursor or Claude, then provide the code to refactor.
