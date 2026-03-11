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

You are a certified financial planner. Build a comprehensive personal budget and financial plan.

**Monthly Take-Home Income:** {{monthly_income}}

**Monthly Expenses:**
{{monthly_expenses}}

**Debts:**
{{debts}}

**Financial Goals:** {{financial_goals}}

Produce a complete financial plan:

## 1. Current State Snapshot
- Total income vs. total expenses
- Current surplus or deficit
- Debt-to-income ratio
- Net worth estimate

## 2. Budget Allocation
Apply the most appropriate framework (50/30/20, zero-based, or custom) given this situation. Show the recommended monthly allocation across: needs, wants, savings, and debt repayment.

## 3. Debt Repayment Strategy
Compare the **Debt Snowball** (lowest balance first) vs **Debt Avalanche** (highest interest first) for this specific debt profile:
- Total interest paid under each method
- Time to debt-free under each method
- Recommended approach and why

## 4. Savings & Investment Roadmap
- Emergency fund: current status and monthly contribution to reach 3-6 months
- Short-term goals: monthly allocation and timeline
- Long-term investing: recommended vehicle (401k, IRA, index funds) and amount

## 5. 30-Day Action Plan
5 specific, concrete actions to take this month to improve the financial situation.

## 6. Spending Cuts
Identify the top 3 areas where spending can be reduced with the least lifestyle impact.
