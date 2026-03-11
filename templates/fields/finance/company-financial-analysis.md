---
id: "company-financial-analysis"
title: "Company Financial Analysis: Memo-Ready Deep Dive"
description: "Analyze a company's financial health and produce a structured memo covering revenue quality, profitability, debt, cash flow, and red flags."
category: "fields/finance"
tags: ["financial-analysis", "company", "due-diligence", "investing", "CFO", "finance", "memo"]
variables:
  - name: "company"
    label: "Company Name / Ticker"
    required: true
  - name: "financials"
    label: "Financial Data (paste P&L, balance sheet highlights, or key metrics you have)"
    required: true
  - name: "analysis_purpose"
    label: "Purpose (e.g. investment decision, acquisition due diligence, competitive benchmarking)"
    required: true
  - name: "comparison"
    label: "Comparison (peer companies or industry benchmarks to compare against)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for conducting a company financial analysis.

The prompt is configured for the following inputs:
- Company: {{company}}
- Financial data: {{financials}}
- Analysis purpose: {{analysis_purpose}}
- Peer comparison: {{comparison}}

The generated prompt must instruct the AI agent to:

1. Act as a senior equity analyst writing a memo that delivers a clear verdict for the stated purpose
2. Write a financial analysis memo with these sections:
   - **Executive Summary**: 3 sentences — the financial health in plain English, the overall bullish or bearish assessment, and the single biggest driver
   - **Revenue Quality**: revenue trend (growth rate, acceleration/deceleration), composition (recurring vs. one-time, concentration risk), and predictability
   - **Profitability**: gross margin trend and comparison to peers, operating leverage (are margins expanding with revenue?), and EBITDA/net income quality with any non-recurring items flagged
   - **Balance Sheet Strength**: cash position and runway, debt load and coverage ratios, working capital dynamics
   - **Cash Flow Analysis**: FCF vs. net income as a quality check, capex intensity, cash conversion cycle
   - **Red Flags**: any concerning patterns — accounting irregularities, deteriorating metrics, covenant risk, management changes
   - **Peer Comparison**: how the company compares to the specified peers on the most important metrics for the stated purpose
   - **Conclusion**: a single clear takeaway — financially fit, at risk, or requires monitoring — framed specifically for the stated analysis purpose

Output: the complete task delegation prompt only. Ready for Claude or a financial agent.
