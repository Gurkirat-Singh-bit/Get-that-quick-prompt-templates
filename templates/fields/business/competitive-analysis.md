---
id: "competitive-analysis"
title: "Competitive Analysis: Landscape Mapping & Positioning"
description: "Map the competitive landscape, identify differentiation opportunities, and surface your unique strategic position."
category: "fields/business"
tags: ["competitive-analysis", "strategy", "positioning", "market", "business", "research"]
variables:
  - name: "your_product"
    label: "Your Product / Company (brief description)"
    required: true
  - name: "competitors"
    label: "Competitors to Analyze (list 3-6 by name)"
    required: true
  - name: "market"
    label: "Market / Category (what space are you competing in?)"
    required: true
  - name: "focus"
    label: "Analysis Focus (e.g. pricing, features, positioning, go-to-market)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for conducting a competitive landscape analysis.

The prompt is configured for the following inputs:
- Your product: {{your_product}}
- Competitors: {{competitors}}
- Market: {{market}}
- Analysis focus: {{focus}}

The generated prompt must instruct the AI agent to:

1. Act as a senior strategy consultant producing an actionable competitive analysis
2. Build a market map describing where each competitor sits on key positioning axes (e.g. price vs. capability, self-serve vs. enterprise, broad vs. specialized)
3. Produce a competitor profile for each listed competitor covering: core value proposition (what they claim vs. what they actually deliver), the customer profile they actually win with, genuine strengths, areas where customers complain or churn, and business model
4. Create a feature and capability comparison matrix across all competitors and the user's product on the dimensions most relevant to the specified analysis focus
5. Identify white space opportunities — customer needs currently underserved by the competitive field, and positioning that is unclaimed
6. Close with a differentiation recommendation: where the user's product should focus its differentiation, what message cuts through, and what capability needs to be built or emphasized

Output: the complete task delegation prompt only. Ready for Claude or a strategy-capable agent.
