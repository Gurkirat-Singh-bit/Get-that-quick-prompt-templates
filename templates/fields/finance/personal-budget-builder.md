---
id: "personal-budget-builder"
title: "Personal Budget Builder: Income, Debt & Savings Plan"
description: "Build a realistic personal budget with debt repayment strategy, savings goals, and monthly action plan — using the right allocation method for your situation."
category: "fields/finance"
tags: ["personal-finance", "budget", "debt", "savings", "investing", "reddit", "money"]
variables:
  - name: "monthly_income"
    label: "Monthly Take-Home Income (after tax)"
    required: true
  - name: "monthly_expenses"
    label: "Monthly Expenses (list categories and amounts, e.g. rent $1200, food $400, subscriptions $80)"
    required: true
  - name: "debts"
    label: "Debts (list each: type, balance, interest rate, minimum payment)"
    required: false
  - name: "financial_goals"
    label: "Financial Goals (e.g. 6-month emergency fund, pay off student loans, invest $500/month)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for building a personal financial plan.

The prompt is configured for the following inputs:
- Monthly income: {{monthly_income}}
- Monthly expenses: {{monthly_expenses}}
- Debts: {{debts}}
- Financial goals: {{financial_goals}}

The generated prompt must instruct the AI agent to:

1. Act as a certified financial planner building an honest, actionable personal financial plan
2. Produce a complete plan with these sections:
   - **Current State Snapshot**: total income vs. total expenses, current monthly surplus or deficit, debt-to-income ratio, and net worth estimate
   - **Budget Allocation**: select the most appropriate framework (50/30/20, zero-based, or custom) given the specific situation, and show the recommended monthly allocation across needs, wants, savings, and debt repayment in dollar amounts
   - **Debt Repayment Strategy**: compare Debt Snowball (lowest balance first) vs. Debt Avalanche (highest interest first) for this specific debt profile — show total interest paid and time to debt-free under each method, then make a clear recommendation with reasoning
   - **Savings and Investment Roadmap**: emergency fund current status and monthly contribution needed to reach 3–6 months of expenses; short-term goal allocations with timelines; long-term investment vehicle recommendations (401k, IRA, index funds) with specific monthly amounts
   - **30-Day Action Plan**: 5 specific, concrete actions to take this month — not generic advice, but actions tied directly to the actual numbers
   - **Top 3 Spending Cuts**: identify where spending can be reduced with the least lifestyle impact, with estimated monthly savings for each

Output: the complete task delegation prompt only. Ready for Claude.
