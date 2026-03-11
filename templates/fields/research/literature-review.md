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

Generate a task delegation prompt for structuring a literature review.

The prompt is configured for the following variables: research topic, academic field, scope, key papers or themes already known, and the researcher's planned contribution.

The generated prompt must instruct the AI agent to:

1. Act as an experienced academic researcher and thesis advisor helping to map and frame a body of literature
2. Recommend a search strategy: which databases to use (Google Scholar, PubMed, JSTOR, Semantic Scholar, etc.), specific search terms and Boolean combinations, and inclusion/exclusion criteria for selecting papers within the defined scope
3. Organize the existing literature into 4–6 thematic streams, for each stream: state the core argument or claim, note key representative studies, describe the methodological approaches used, and trace how thinking has evolved over time
4. Identify areas of consensus, active debates or contradictions, and methodological disputes in the field
5. Surface 3–5 significant research gaps — questions unanswered, populations unstudied, methods not applied, or contradictions unresolved
6. Explain how the researcher's planned contribution addresses one or more of these gaps and position it clearly within the landscape
7. Suggest a written review outline with headings and subheadings

Output: the complete task delegation prompt only. Ready for Claude or a research agent.
