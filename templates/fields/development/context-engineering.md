---
id: "context-engineering"
title: "Context Engineering: AI Coding Agent System Prompt"
description: "Generate a system prompt that configures an AI coding agent with full project context — ready to paste into Claude Projects, Cursor, or any coding agent."
category: "fields/development"
tags: ["context-engineering", "system-prompt", "coding-agent", "cursor", "claude", "karpathy"]
variables:
  - name: "project_name"
    label: "Project Name"
    required: true
  - name: "tech_stack"
    label: "Tech Stack (languages, frameworks, key dependencies)"
    required: true
  - name: "architecture_summary"
    label: "Architecture Summary (how the system is structured)"
    required: true
  - name: "conventions"
    label: "Coding Conventions (naming, style, patterns to follow)"
    required: true
  - name: "current_task"
    label: "Current Task or Focus Area"
    required: true
  - name: "off_limits"
    label: "Off-Limits (files, patterns, or approaches to never touch)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a complete system prompt to configure a coding AI agent for {{project_name}}. This will be pasted into Claude Projects, Cursor system prompt, or an API system parameter.

The system prompt must:

1. **Establish project identity:** {{project_name}}, stack: {{tech_stack}}, architecture: {{architecture_summary}}
2. **Lock in conventions:** {{conventions}} — these are non-negotiable. The agent enforces them in every file it touches.
3. **Set current focus:** {{current_task}} — the agent knows what it is working on
4. **Hard constraints:** {{off_limits}} — files and patterns the agent must never modify or introduce
5. **Behavioral rules to include:**
   - Always read the relevant existing code before writing new code
   - Restate the task before implementing it
   - Flag every assumption made
   - Write tests for any new logic
   - Never introduce new dependencies without stating why and asking for confirmation
   - If something looks wrong in existing code, call it out rather than silently working around it

Output: the complete agent system prompt only. Tightly written, no fluff. The agent using this should need no further orientation before starting work.
