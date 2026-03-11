---
id: "investment-thesis"
title: "Investment Thesis: Research & Conviction Builder"
description: "Build a structured investment thesis for any asset — covering the core narrative, catalysts, risks, valuation, and sizing rationale."
category: "fields/finance"
tags: ["investing", "thesis", "stocks", "crypto", "venture", "analysis", "finance"]
variables:
  - name: "asset"
    label: "Asset (stock ticker, crypto, fund, private company, real estate market)"
    required: true
  - name: "investment_type"
    label: "Investment Type (long-term hold, swing trade, VC bet, real estate)"
    required: true
  - name: "known_info"
    label: "What You Know (paste key facts, financials, news, or just the ticker)"
    required: true
  - name: "portfolio_context"
    label: "Portfolio Context (risk tolerance, time horizon, existing exposure)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are a seasoned investment analyst. Build a structured investment thesis for the following.

**Asset:** {{asset}}
**Investment Type:** {{investment_type}}
**Known Information:**
{{known_info}}
**Portfolio Context:** {{portfolio_context}}

Structure the thesis as follows:

## 1. The Core Narrative (2-3 sentences)
What is the simple, compelling story? Why does this asset have more upside than the market currently prices?

## 2. Why Now
What has changed recently — or what will change — that makes this the right time to invest? (Catalyst, inflection point, mispricing, structural shift)

## 3. Bull Case
The scenario where this investment works as hoped. What needs to be true? What are the key milestones?

## 4. Bear Case & Risk Factors
The strongest arguments against this investment. What could go wrong? What would cause you to be wrong about the core narrative?

## 5. Valuation
Is this cheap, fairly valued, or expensive? Use at least one relevant metric (P/E, P/S, DCF estimate, comparable transactions, token fundamentals).

## 6. Variant View
What does the market consensus believe? Where does this thesis disagree with consensus, and why is that disagreement valid?

## 7. Position Sizing Rationale
Given the risk/reward and portfolio context, what % allocation is appropriate? What would trigger adding or reducing the position?

## 8. Exit Criteria
What would cause you to sell: a target price hit, a thesis-breaking event, or a time-based review?
