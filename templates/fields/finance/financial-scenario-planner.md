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

Generate a task delegation prompt for financial scenario modeling.

The prompt is configured for the following inputs:
- Decision: {{decision}}
- Current financials: {{current_financials}}
- Timeframe: {{timeframe}}
- Key assumptions: {{key_assumptions}}

The generated prompt must instruct the AI agent to:

1. Act as a senior CFO and financial modeler building a decision-quality scenario analysis
2. Build three scenarios with explicit, named assumptions and projected financials for each:
   - **Base Case (Most Likely)**: core assumptions for growth, conversion, churn, and cost; projected revenue, costs, and net impact over the timeframe; key milestones and inflection points
   - **Bull Case (Optimistic)**: name specifically what goes better than expected and why — not just "everything works" — with revised assumptions, resulting financials, and an estimated probability
   - **Bear Case (Pessimistic)**: name specifically what goes wrong and why — realistic risks, not catastrophic failure — with revised assumptions, resulting financials, and a minimum floor estimate with probability
3. Produce a sensitivity table for the top 2–3 variables that most swing the outcome, showing how the result changes if each moves ±20%
4. Assign a probability estimate to each scenario that sums to 100%
5. Close with a clear recommendation: given the three scenarios, what is the financially sound decision? State what conditions would change the recommendation and what hedging actions reduce downside without sacrificing meaningful upside

Output: the complete task delegation prompt only. Ready for Claude or a financial analysis agent.
