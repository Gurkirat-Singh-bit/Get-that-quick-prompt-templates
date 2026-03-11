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

You are a senior equity analyst. Analyze the following company's financial health and write a memo.

**Company:** {{company}}
**Purpose:** {{analysis_purpose}}
**Comparison Benchmarks:** {{comparison}}

**Financial Data:**
{{financials}}

Produce a financial analysis memo:

## Executive Summary (3 sentences)
The financial health in plain English. Bullish or bearish overall assessment and the single biggest driver.

## Revenue Quality
- Revenue trend (growth rate, acceleration/deceleration)
- Revenue composition (recurring vs. one-time, concentration risk)
- Revenue predictability and visibility

## Profitability
- Gross margin trend and vs. peers
- Operating leverage (are margins expanding as revenue grows?)
- EBITDA and net income quality (any non-recurring items?)

## Balance Sheet Strength
- Cash position and runway
- Debt load and coverage ratios
- Working capital dynamics

## Cash Flow Analysis
- FCF generation vs. net income (quality check)
- Capex intensity
- Cash conversion cycle

## Red Flags
Any concerning patterns: accounting irregularities, deteriorating metrics, covenant risk, management changes.

## Peer Comparison
How does {{company}} compare to {{comparison}} across the most important metrics?

## Conclusion
Financially fit, at risk, or requires monitoring? One clear takeaway for the stated purpose.
