---
id: "pain-framework"
title: "PAIN Framework: Problem-to-Action Agent Prompt"
description: "Generate a PAIN-structured prompt to delegate problem analysis and persuasive action planning to an AI agent."
category: "frameworks/goal-oriented"
tags: ["pain", "framework", "problem-solving", "persuasion", "agent", "delegation"]
variables:
  - name: "problem"
    label: "Problem (the core challenge to address)"
    required: true
  - name: "audience"
    label: "Audience (who is affected or needs to act)"
    required: true
  - name: "insight"
    label: "Insight (key understanding or root cause, if known)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a PAIN-framework agent prompt to delegate problem analysis and action planning.

Configure it for:
- Problem: {{problem}}
- Audience: {{audience}}
- Known insight: {{insight}}

The generated prompt must instruct the agent to:
1. **P — Problem:** Clearly restate {{problem}} from the perspective of {{audience}} — in their words, not abstract language
2. **A — Amplify:** Expand on the real cost of this problem — time, money, risk, emotional weight — and make it concrete for {{audience}}
3. **I — Insight:** Use {{insight}} if provided, or independently identify the non-obvious root cause that most solutions miss
4. **N — Next Steps:** Produce a prioritized, actionable list of next steps specifically for {{audience}} — immediate actions first

The prompt should produce output that moves {{audience}} from awareness → urgency → understanding → action.

Output: the complete PAIN agent prompt only. Ready to delegate to Claude, GPT, or a writing-capable AI agent.
