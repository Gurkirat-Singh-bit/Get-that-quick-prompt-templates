---
id: "risen-framework"
title: "RISEN Framework: Role, Instructions, Steps, End Goal, Narrowing"
description: "A comprehensive 5-part framework for precise, repeatable prompts — define Role, Instructions, Steps, End Goal, and Narrowing constraints."
category: "frameworks/structured"
tags: ["risen", "framework", "role", "instructions", "steps", "goal", "constraints", "intermediate"]
variables:
  - name: "role"
    label: "Role (expert persona for the AI)"
    required: true
  - name: "instructions"
    label: "Instructions (what needs to be done)"
    required: true
  - name: "end_goal"
    label: "End Goal (final desired outcome)"
    required: true
  - name: "constraints"
    label: "Narrowing/Constraints (scope, tone, format, limitations)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

**Role:** You are {{role}}.

**Instructions:** {{instructions}}

**Steps:** Break this task into clear, sequential steps. Think through each phase before executing and show your progression explicitly.

**End Goal:** {{end_goal}}

**Narrowing:** Apply the following constraints throughout: {{constraints}}

Follow this structure to deliver a complete, goal-aligned response that stays within the defined scope.
