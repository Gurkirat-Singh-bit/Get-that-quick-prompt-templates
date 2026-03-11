---
id: "tech-debt-analysis"
title: "Tech Debt Analyst: Task Delegation Prompt"
description: "Generate a task prompt to delegate tech debt analysis to an AI agent — produces an inventory, impact scoring, and 90-day remediation plan."
category: "fields/development"
tags: ["tech-debt", "agent", "delegation", "architecture", "planning", "engineering"]
variables:
  - name: "codebase_description"
    label: "Codebase Description (what it does, age, size, team)"
    required: true
  - name: "pain_points"
    label: "Known Pain Points (what slows the team down or breaks often)"
    required: true
  - name: "business_context"
    label: "Business Context (growth phase, upcoming launches, constraints)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a tech debt analysis task prompt to delegate to an AI engineering agent.

Configure it for:
- Codebase: {{codebase_description}}
- Pain points: {{pain_points}}
- Business context: {{business_context}}

The generated prompt must instruct the agent to:
1. Act as a senior engineering lead conducting a tech debt audit
2. Categorize each pain point: deliberate debt (known shortcuts), accidental debt (poor decisions), or bit rot (aged code)
3. Score each item on: developer velocity impact (1-5), production risk (1-5), onboarding friction (1-5)
4. Classify each as: Quick Win (low effort, high impact) | Strategic Investment (high effort, high value) | Accept and Document (deprioritize)
5. Produce a 90-day remediation plan in three phases: weeks 1-4, 5-8, 9-12 — balancing debt reduction with feature delivery

Output: the complete tech debt analysis task prompt only. Ready to hand to Claude or an engineering-focused AI agent, along with codebase context.
