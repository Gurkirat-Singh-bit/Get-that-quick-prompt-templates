---
id: "financial-scenario-planner"
title: "Financial Scenario Planner: Bull / Base / Bear Analysis"
description: "Model three financial scenarios for any decision — base case, optimistic, and pessimistic — with sensitivity analysis and a recommendation."
category: "fields/finance"
tags: ["finance", "scenario-planning", "modeling", "forecasting", "decision-making", "CFO"]
variables:
  - name: "decision"
    label: "Financial Decision (e.g. hiring 5 engineers, launching a new product, raising prices 15%)"
    required: true
  - name: "current_financials"
    label: "Current Financials (revenue, costs, margins, burn rate — whatever is relevant)"
    required: true
  - name: "timeframe"
    label: "Timeframe (e.g. 12 months, 3 years)"
    required: true
  - name: "key_assumptions"
    label: "Key Assumptions (growth rate, churn, conversion — your current best guesses)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are a senior CFO and financial modeler. Model three scenarios for the following decision.

**Decision:** {{decision}}
**Current Financials:** {{current_financials}}
**Timeframe:** {{timeframe}}
**Key Assumptions:** {{key_assumptions}}

Build a scenario analysis with three cases:

## Base Case (Most Likely)
- Core assumptions (growth, conversion, churn, cost)
- Projected revenue, costs, and net impact over {{timeframe}}
- Key milestones and inflection points

## Bull Case (Optimistic)
- What goes better than expected and why (be specific, not just "everything works")
- Revised assumptions and resulting financials
- Maximum upside and probability estimate

## Bear Case (Pessimistic)
- What goes wrong and why (the realistic risks, not catastrophic ones)
- Revised assumptions and resulting financials
- Minimum floor and probability estimate

## Sensitivity Table
Identify the 2-3 variables that swing the outcome most. Show how the result changes if each moves ±20%.

## Recommendation
Given the three scenarios, what is the financially sound decision? What conditions would change that recommendation? What hedging actions reduce downside without sacrificing upside?
