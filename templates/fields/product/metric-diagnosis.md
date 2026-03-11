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

You are a senior product analyst. The following metric anomaly needs investigation.

**Metric:** {{metric}}
**Observed Change:** {{change}}
**Product Context:** {{product_context}}
**Recent Changes:** {{recent_changes}}

Structure your analysis as follows:

## 1. Decomposition
Break the metric into its component parts. For example, DAU = (new users + retained users + reactivated users). Identify which sub-metric is most likely to have moved.

## 2. Hypotheses
Generate 5-8 specific, falsifiable hypotheses for what caused this change. For each:
- State the hypothesis clearly
- Rate the likelihood: High / Medium / Low
- State what data or signal would confirm or disprove it

## 3. Investigation Checklist
Priority-ordered list of queries, dashboards, or external checks to run. Map each to a hypothesis.

## 4. Instrumentation Gaps
Identify any missing tracking or data that would make this faster to diagnose in the future.

## 5. Recommended Actions
Based on the most likely hypotheses, what should the team do right now vs. monitor and wait?
