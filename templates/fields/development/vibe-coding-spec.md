---
id: "vibe-coding-spec"
title: "Vibe Coding Spec: AI-First Build Agent Prompt"
description: "Generate a task prompt to delegate a full project build to an AI coding agent — structured so Claude or Cursor can build iteratively with minimal back-and-forth."
category: "fields/development"
tags: ["vibe-coding", "build", "cursor", "claude", "agent", "karpathy", "delegation"]
variables:
  - name: "project_name"
    label: "Project Name"
    required: true
  - name: "what_it_does"
    label: "What It Does (plain English, 1-3 sentences)"
    required: true
  - name: "target_user"
    label: "Target User and the Problem It Solves"
    required: true
  - name: "core_features"
    label: "Core Features (3-5 must-haves for v1)"
    required: true
  - name: "tech_preferences"
    label: "Tech Preferences (stack or 'you decide')"
    required: true
  - name: "out_of_scope"
    label: "Out of Scope for v1 (explicit non-goals)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a complete build task prompt for {{project_name}} to delegate to an AI coding agent (Claude, Cursor, or similar). The agent should be able to start building from this prompt alone.

The generated prompt must instruct the agent to:

1. **Understand the product:** {{what_it_does}} built for {{target_user}}
2. **Build only this in v1:** {{core_features}} — nothing more
3. **Tech:** {{tech_preferences}}
4. **Never build:** {{out_of_scope}}

Include these build rules in the prompt:
- Define the data model first — show the schema before writing any UI
- Start with mock/static data — no real database until the UI renders correctly
- One feature at a time — complete and verify before moving to the next
- Split into multiple focused files — no file over 200 lines
- After each feature: summarize what was built, what's next, and any decisions made
- Ask clarifying questions before starting, not during

Output: the complete build task prompt only. Dense, specific, and structured so the coding agent can build the entire v1 iteratively. Ready for Cursor, Claude, or any code-generating AI agent.
