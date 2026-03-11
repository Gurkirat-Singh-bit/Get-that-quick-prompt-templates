---
id: "literature-review"
title: "Literature Review: Structured Academic Survey"
description: "Generate a structured literature review outline — map existing research, identify gaps, synthesize themes, and frame your contribution."
category: "fields/research"
tags: ["research", "literature-review", "academic", "thesis", "survey", "synthesis"]
variables:
  - name: "research_topic"
    label: "Research Topic or Question"
    required: true
  - name: "field"
    label: "Academic Field or Discipline"
    required: true
  - name: "scope"
    label: "Scope (e.g. last 10 years, seminal works only, specific methodology)"
    required: true
  - name: "papers_or_themes"
    label: "Key Papers or Themes You Already Know (optional starting point)"
    required: false
  - name: "your_contribution"
    label: "Your Research Angle (what you plan to add or argue)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are an experienced academic researcher and thesis advisor. Produce a structured literature review.

**Topic:** {{research_topic}}
**Field:** {{field}}
**Scope:** {{scope}}
**Known Works:** {{papers_or_themes}}
**Your Contribution:** {{your_contribution}}

Structure the literature review as follows:

## 1. Search Strategy
- Recommended databases and search engines (Google Scholar, PubMed, JSTOR, Semantic Scholar, etc.)
- Key search terms and Boolean combinations to use
- Inclusion/exclusion criteria for selecting papers

## 2. Thematic Map
Organize the existing literature into 4-6 major themes or schools of thought. For each:
- Core argument or claim of this body of work
- Key representative studies (even if hypothetical given scope)
- Methodological approaches used
- Evolution of thinking over time

## 3. Agreements & Debates
- What do researchers broadly agree on?
- Where are the active debates or contradictions?
- What methodological disputes exist?

## 4. Research Gaps
The 3-5 most significant gaps in the literature — questions that remain unanswered, populations unstudied, methods not applied, or contradictions unresolved.

## 5. How Your Work Fits
Explain how {{your_contribution}} addresses one or more of these gaps. Position it clearly within the landscape.

## 6. Recommended Review Structure
A suggested outline for the actual written literature review (headings and subheadings).
