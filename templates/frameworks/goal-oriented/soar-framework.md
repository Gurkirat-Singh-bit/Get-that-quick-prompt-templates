---
id: "soar-framework"
title: "SOAR Framework: Strategic Analysis Agent Prompt"
description: "Generate a SOAR-structured agent prompt to delegate forward-looking strategic analysis — Strengths, Opportunities, Aspirations, Results."
category: "frameworks/goal-oriented"
tags: ["soar", "framework", "strategy", "analysis", "agent", "delegation", "planning"]
variables:
  - name: "subject"
    label: "Subject (organization, product, team, or individual to analyze)"
    required: true
  - name: "context"
    label: "Context (current state, industry, relevant background)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a SOAR strategic analysis agent prompt.

Configure it for:
- Subject: {{subject}}
- Context: {{context}}

The generated prompt must instruct the agent to produce a SOAR analysis:
1. **Strengths:** Current core capabilities, competitive advantages, and assets — evidence-based, not aspirational
2. **Opportunities:** External conditions, trends, and gaps that {{subject}} can act on right now
3. **Aspirations:** The ideal future state — specific, compelling, and grounded enough to drive decisions
4. **Results:** Measurable outcomes that would confirm the aspirations are being achieved — KPIs, milestones, observable changes

Close with a strategic narrative that connects Strengths → Opportunities → Aspirations → Results in a coherent arc.

Output: the complete SOAR agent prompt only. The receiving agent should produce a strategic document that is genuinely useful for planning and decision-making. Ready for Claude or any analytical AI agent.
