---
id: "research-synthesis"
title: "Research Synthesis: Multi-Source Evidence Summary"
description: "Synthesize findings from multiple research sources into a coherent, well-structured summary with agreements, contradictions, confidence levels, and implications."
category: "fields/research"
tags: ["research", "synthesis", "evidence", "analysis", "academic", "summary", "meta-analysis"]
variables:
  - name: "research_question"
    label: "Research Question or Topic"
    required: true
  - name: "sources"
    label: "Sources to Synthesize (paste abstracts, summaries, or key findings from each)"
    required: true
  - name: "audience"
    label: "Audience for the Synthesis (e.g. academic paper, executive brief, policy memo)"
    required: true
  - name: "output_length"
    label: "Output Length (e.g. 500-word summary, full synthesis, bullet points)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are a senior research analyst. Synthesize the following sources into a coherent summary.

**Research Question:** {{research_question}}
**Audience:** {{audience}}
**Output Length:** {{output_length}}

**Sources:**
{{sources}}

Produce a structured synthesis:

## 1. Executive Summary
3-5 sentences capturing the most important finding across all sources. What does the evidence say, overall?

## 2. Areas of Consensus
What do the sources agree on? Cite which sources align and on what specific points.

## 3. Contradictions & Conflicts
Where do sources disagree? What might explain the contradiction (methodology, context, date, population)?

## 4. Evidence Quality Assessment
For each source or finding, assess:
- Study design strength (RCT, observational, case study, expert opinion)
- Sample size and generalizability
- Potential biases or conflicts of interest
- Overall confidence level: High / Medium / Low

## 5. Key Findings (Ranked by Evidence Strength)
The most important, best-supported findings, ordered from strongest to weakest evidence.

## 6. Gaps & Uncertainties
What does this body of evidence not answer? What would stronger evidence require?

## 7. Implications
For the stated audience: what should they believe, decide, or investigate further based on this synthesis?
