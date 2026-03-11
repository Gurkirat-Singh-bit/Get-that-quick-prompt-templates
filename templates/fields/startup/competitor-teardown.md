---
id: "competitor-teardown"
title: "Competitor Teardown: Strategic Analysis of a Rival"
description: "Deeply analyze a competitor — their business model, strengths, weaknesses, positioning gaps, and how to win against them."
category: "fields/startup"
tags: ["startup", "competitive-intelligence", "strategy", "positioning", "competitor", "founder"]
variables:
  - name: "competitor"
    label: "Competitor Name"
    required: true
  - name: "your_company"
    label: "Your Company / Product (brief description)"
    required: true
  - name: "known_info"
    label: "Known Information About the Competitor (funding, pricing, customers, reviews, news)"
    required: true
  - name: "battleground"
    label: "Where You Compete (which customer segment or use case is contested?)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for conducting a deep competitor teardown.

The prompt is configured for the following inputs:
- Competitor: {{competitor}}
- Your company: {{your_company}}
- Known information: {{known_info}}
- Battleground: {{battleground}}

The generated prompt must instruct the AI agent to:

1. Act as a senior competitive intelligence analyst tearing down the competitor from the perspective of the user's company — the goal is actionable intelligence, not a balanced essay
2. Analyze the competitor's business model: how they make money (pricing, tiers, expansion revenue), who their actual ICP is inferred from behavior (not just stated), and what their acquisition strategy is (SEO, sales, PLG, partnerships)
3. Honestly assess where they are genuinely strong — what they do better than anyone and what would make a customer choose them over the user's product
4. Identify where they are weak or vulnerable: product gaps inferred from reviews and community complaints, strategic blind spots (markets they ignore, segments they underserve), and organizational debt (legacy tech, slow release cadence, heavy sales motion)
5. Predict their competitive playbook: how they will respond when they lose a deal to the user's company and what their likely counter-move is
6. Provide specific, non-generic tactics for winning in the contested battleground: positioning language that makes differences concrete, use cases where the user wins by default, and which customer profiles to prioritize vs. avoid
7. Produce a watch list of 2–3 signals that would indicate the competitor's strategy is changing in ways that create new threats

Output: the complete task delegation prompt only. Ready for Claude or a competitive intelligence agent.
