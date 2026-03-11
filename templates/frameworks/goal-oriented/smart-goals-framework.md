---
id: "smart-goals-framework"
title: "SMART Goals: Goal-to-Plan Agent Prompt"
description: "Generate a SMART goals prompt to delegate goal structuring to an AI agent — turns a vague ambition into a specific, measurable, actionable plan."
category: "frameworks/goal-oriented"
tags: ["smart", "goals", "planning", "agent", "delegation", "productivity"]
variables:
  - name: "goal_area"
    label: "Goal Area (what you want to achieve)"
    required: true
  - name: "timeframe"
    label: "Timeframe (deadline or time horizon)"
    required: true
  - name: "context"
    label: "Context (current situation, resources, constraints)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a SMART goals agent prompt that will be handed to Claude or another AI to transform a vague goal into a structured, actionable plan.

Configure it for:
- Goal area: {{goal_area}}
- Timeframe: {{timeframe}}
- Context: {{context}}

The generated prompt must instruct the agent to:
1. Take {{goal_area}} and {{context}} as input
2. Transform it into a SMART goal: Specific, Measurable, Achievable, Relevant, Time-bound
3. For each SMART dimension: apply it to the goal and explain the implication
4. Produce: a single SMART goal statement + a phased action plan with milestones mapped to {{timeframe}}
5. Flag any assumptions made about feasibility or resources

Output: the complete agent prompt only. The receiving agent should be able to produce a polished SMART goal plan without any follow-up. Ready for Claude, GPT, or any planning-capable AI.
