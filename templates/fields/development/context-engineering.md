---
id: "context-engineering"
title: "Context Engineering: Fill the Window Right"
description: "Karpathy-inspired context engineering — load the AI's context window with exactly the right code, data, and instructions for each step of a complex task."
category: "fields/development"
tags: ["context-engineering", "karpathy", "llm", "agentic", "workflow", "advanced", "coding"]
variables:
  - name: "task"
    label: "Task (what needs to be built or solved?)"
    required: true
  - name: "relevant_code"
    label: "Relevant Code/Files (paste the most relevant code snippets or describe the files)"
    required: true
  - name: "tech_stack"
    label: "Tech Stack (languages, frameworks, dependencies)"
    required: true
  - name: "constraints"
    label: "Constraints (performance, security, style guide, existing patterns to follow)"
    required: true
  - name: "current_state"
    label: "Current State (what exists, what is broken, or what is missing)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are a senior software engineer working in the following context:

**Tech Stack:** {{tech_stack}}

**Current State of the Codebase:**
{{current_state}}

**Relevant Code:**
```
{{relevant_code}}
```

**Task:**
{{task}}

**Constraints to follow exactly:**
{{constraints}}

Before writing any code:
1. Restate the task in your own words to confirm understanding.
2. Identify any ambiguities or missing information and state your assumptions.
3. Describe your approach at a high level before implementing.

Then implement the task. After implementation:
- Explain what you changed and why.
- Flag any edge cases, risks, or follow-up work needed.
- If anything in the provided code looks incorrect or fragile, call it out.
