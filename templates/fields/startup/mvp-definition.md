---
id: "mvp-definition"
title: "MVP Definition: Scope, Assumptions & Success Criteria"
description: "Define the smallest possible product that tests your riskiest assumptions — with a clear build scope, what to cut, and how to know if it worked."
category: "fields/startup"
tags: ["startup", "mvp", "product", "validation", "lean", "founder", "build"]
variables:
  - name: "product_idea"
    label: "Product Idea (what you want to build)"
    required: true
  - name: "target_user"
    label: "Target User (who is this for?)"
    required: true
  - name: "core_hypothesis"
    label: "Core Hypothesis (the belief your business depends on being true)"
    required: true
  - name: "resources"
    label: "Resources Available (team size, time, budget)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for defining a minimum viable product.

The prompt is configured for the following inputs:
- Product idea: {{product_idea}}
- Target user: {{target_user}}
- Core hypothesis: {{core_hypothesis}}
- Resources: {{resources}}

The generated prompt must instruct the AI agent to:

1. Act as a lean startup advisor whose job is to help the founder build as little as possible while learning as much as possible
2. List all major assumptions this business depends on being true, rank them from most to least risky (most likely to kill the idea if wrong), and identify that the MVP must test assumption #1
3. Define the minimum feature set that tests the riskiest assumption — for each included feature: why it is necessary (which assumption it tests) and an estimated build time
4. List features that feel important but are not needed for validation, with a reason why each is being deferred
5. Identify whether the hypothesis can be validated without building software first — describe a specific non-product validation approach (landing page, concierge MVP, Wizard of Oz, fake door test, sales calls) if applicable
6. Define success criteria: the specific metric that would confirm or deny the hypothesis, the minimum threshold that justifies building further, and the timeline for collecting meaningful signal
7. If building is the right path, specify the optimal build sequence — what to ship first, what can be parallelized, what is sequential
8. Define kill criteria before building starts — the specific result that would signal it is time to stop, pivot, or start over, so the goalposts cannot be moved later

Output: the complete task delegation prompt only. Ready for Claude or a product strategy agent.
