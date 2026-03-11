---
id: "investor-pitch-memo"
title: "Investor Pitch Memo: YC-Style 1-Page Investment Brief"
description: "Write a compelling 1-page investor memo — problem, solution, traction, why now, team, and ask — in the concise style that top investors actually read."
category: "fields/startup"
tags: ["startup", "fundraising", "investor", "pitch", "YC", "VC", "memo", "founder"]
variables:
  - name: "company_name"
    label: "Company Name"
    required: true
  - name: "one_liner"
    label: "One-Liner (what you do in one sentence)"
    required: true
  - name: "problem"
    label: "Problem (what painful problem exists? who has it?)"
    required: true
  - name: "solution"
    label: "Solution (what you built and how it works)"
    required: true
  - name: "traction"
    label: "Traction (revenue, users, growth rate, notable customers — be specific)"
    required: true
  - name: "market"
    label: "Market Size (TAM/SAM/SOM or just the honest opportunity)"
    required: true
  - name: "team"
    label: "Team (founders' relevant backgrounds and why you)"
    required: true
  - name: "ask"
    label: "The Ask (how much you're raising, at what valuation, what it funds)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for writing a YC-style investor pitch memo.

The prompt is configured for the following variables: company name, one-liner, problem, solution, traction, market, team, and ask.

The generated prompt must instruct the AI agent to:

1. Act as a YC partner who has reviewed thousands of applications — writing a memo that earns a second read through radical concision and specificity
2. Write a tight 1-page memo with zero filler, zero vague claims, and zero buzzwords — every word must earn its place:
   - **Company name and one-liner**: hook the reader in the first line
   - **The Problem**: 2–3 sentences making the pain visceral and specific — who suffers, how often, and what it costs them
   - **The Solution**: 2–3 sentences on what was built, how it works, and the core insight that makes it work (mechanism, not just claim)
   - **Why Now**: 1–2 sentences on what has changed in the world that makes this the right moment
   - **Traction**: bullet points only, hard numbers — growth rate matters more than absolute size, be honest
   - **Market**: describe the real opportunity — who is paying for what today and how the company expands — not "trillion-dollar market" theater
   - **Team**: why are these specific people the ones to build this — unfair advantages, domain insight, relevant experience
   - **The Ask**: amount, terms if set, use of funds in 3 bullets, and what milestone it reaches
3. After the memo, generate the 3 hardest questions an investor will ask about this specific company and write a prepared answer for each

Output: the complete task delegation prompt only. Ready for Claude.
