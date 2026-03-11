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

Generate a task delegation prompt for writing a structured investment thesis.

The prompt is configured for the following inputs:
- Asset: {{asset}}
- Investment type: {{investment_type}}
- Known information: {{known_info}}
- Portfolio context: {{portfolio_context}}

The generated prompt must instruct the AI agent to:

1. Act as a seasoned investment analyst writing a thesis that is conviction-building, not just descriptive
2. Write a structured thesis with these sections — every section must be grounded in the known information, not generic boilerplate:
   - **Core Narrative**: 2–3 sentences — the simple, compelling story for why this asset has more upside than the market currently prices
   - **Why Now**: what has changed recently (or will change) that creates a catalyst, inflection point, mispricing, or structural shift — not just "good company"
   - **Bull Case**: what needs to be true for this investment to work as hoped, with key milestones
   - **Bear Case**: the strongest honest arguments against this investment, including what would cause the core narrative to be wrong
   - **Valuation**: use at least one relevant metric (P/E, P/S, DCF estimate, comparable transactions, token fundamentals) to assess whether this is cheap, fairly valued, or expensive
   - **Variant View**: what does market consensus believe, where does this thesis disagree with that consensus, and why is the disagreement valid
   - **Position Sizing Rationale**: given the risk/reward profile and portfolio context, what percentage allocation is appropriate and what would trigger adding or reducing
   - **Exit Criteria**: define in advance what would cause a sale — a target price, a thesis-breaking event, or a scheduled review

Output: the complete task delegation prompt only. Ready for Claude or a financial analysis agent.
