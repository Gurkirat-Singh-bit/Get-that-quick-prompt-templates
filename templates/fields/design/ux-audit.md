---
id: "ux-audit"
title: "UX Audit: Usability, Flow & Friction Analysis"
description: "A structured UX audit of a product flow or screen — evaluate usability heuristics, identify friction points, and recommend improvements."
category: "fields/design"
tags: ["ux", "usability", "audit", "heuristics", "friction", "design", "nielsen"]
variables:
  - name: "product"
    label: "Product / Feature (what is being audited?)"
    required: true
  - name: "user_flow"
    label: "User Flow (describe the flow or screens, step by step)"
    required: true
  - name: "user_goal"
    label: "User Goal (what is the user trying to accomplish?)"
    required: true
  - name: "platform"
    label: "Platform (web, iOS, Android, desktop)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for conducting a structured UX audit.

The prompt is configured for the following inputs:
- Product: {{product}}
- User flow: {{user_flow}}
- User goal: {{user_goal}}
- Platform: {{platform}}

The generated prompt must instruct the AI agent to:

1. Act as a senior UX designer with expertise in usability heuristics and conversion optimization
2. Evaluate the described flow against all 10 of Nielsen's Usability Heuristics: Visibility of System Status, Match with Real World, User Control & Freedom, Consistency & Standards, Error Prevention, Recognition over Recall, Flexibility & Efficiency, Aesthetic & Minimalist Design, Error Recovery, and Help & Documentation
3. For every violation found, produce a structured entry with:
   - Severity rating: Critical (blocks task completion) / Major (causes significant frustration) / Minor (polish issue)
   - Which heuristic is violated
   - A specific description of what is wrong and exactly where in the flow it occurs
   - A concrete fix with a rationale explaining why it resolves the issue
4. Conclude with the top 5 highest-impact improvements, ranked by effort-to-impact ratio — include an estimate of effort (Low/Medium/High) and expected impact (Low/Medium/High) for each

Output: the complete task delegation prompt only. Ready for Claude or any UX-capable agent.
