---
id: "metric-diagnosis"
title: "Metric Diagnosis: Investigate a Drop or Spike"
description: "Systematically diagnose an unexpected metric change — structure hypotheses, identify root causes, and recommend actions."
category: "fields/product"
tags: ["metrics", "analytics", "diagnosis", "root-cause", "product", "data", "pm"]
variables:
  - name: "metric"
    label: "Metric (e.g. DAU, conversion rate, churn, revenue)"
    required: true
  - name: "change"
    label: "Change Observed (e.g. 'dropped 18% week-over-week', 'spiked 40% on Tuesday')"
    required: true
  - name: "product_context"
    label: "Product Context (what the product does, typical user behavior)"
    required: true
  - name: "recent_changes"
    label: "Recent Changes (deployments, campaigns, pricing changes in last 2 weeks)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for investigating a metric anomaly.

The prompt is configured for the following inputs:
- Metric: {{metric}}
- Change observed: {{change}}
- Product context: {{product_context}}
- Recent changes: {{recent_changes}}

The generated prompt must instruct the AI agent to:

1. Act as a senior product analyst conducting a structured root-cause investigation
2. Decompose the metric into its component parts (e.g. DAU = new + retained + reactivated users) and identify which sub-metric is the most likely driver of the observed change
3. Generate 5–8 specific, falsifiable hypotheses for what caused the change — for each hypothesis: state it clearly, rate its likelihood (High/Medium/Low), and specify what data or signal would confirm or disprove it
4. Produce a prioritized investigation checklist of queries, dashboards, or external checks to run, with each item mapped to a specific hypothesis
5. Identify instrumentation gaps — missing tracking or data that would make this type of anomaly faster to diagnose in the future
6. Recommend immediate actions vs. monitor-and-wait based on the highest-probability hypotheses — be specific, not generic

Output: the complete task delegation prompt only. Ready for Claude or a data analysis agent.
