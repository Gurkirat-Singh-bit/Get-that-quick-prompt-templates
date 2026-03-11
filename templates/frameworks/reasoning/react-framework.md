---
id: "react-framework"
title: "ReAct Framework: Reasoning + Acting Agent Loop"
description: "Generate a ReAct-structured prompt to configure an AI agent that alternates between reasoning and acting — ideal for Cursor, agentic Claude, or tool-using AI."
category: "frameworks/reasoning"
tags: ["react", "reasoning", "acting", "agentic", "tool-use", "cursor", "claude", "agent"]
variables:
  - name: "task"
    label: "Task (what the agent must accomplish)"
    required: true
  - name: "available_tools"
    label: "Available Tools (what the agent can use: bash, file read, search, APIs, etc.)"
    required: true
  - name: "success_criteria"
    label: "Success Criteria (how the agent knows it's done)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a ReAct (Reasoning + Acting) agent prompt. This is designed for AI agents that have tool access — Claude with tools, Cursor agent mode, or any agentic AI setup.

Configure it for:
- Task: {{task}}
- Available tools: {{available_tools}}
- Done when: {{success_criteria}}

The generated prompt must configure the agent to:
1. Operate in a strict Thought → Action → Observation loop
2. Always write out a "Thought:" before taking any action — explains what it knows and what it plans to do next
3. Take only one "Action:" at a time using the available tools
4. Write an "Observation:" after each action — what changed, what was learned
5. Continue the loop until {{success_criteria}} is met
6. End with a "Final Answer:" that synthesizes all observations

The prompt should also tell the agent: never skip the Thought step, never take multiple actions simultaneously, and stop and report if it gets stuck.

Output: the complete ReAct agent system prompt only. Optimized for Cursor agent mode, Claude with tools, or any MCP-enabled agent workflow.
