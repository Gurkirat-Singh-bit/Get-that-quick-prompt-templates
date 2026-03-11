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

Generate a task delegation prompt for synthesizing findings from multiple research sources.

The prompt is configured for the following variables: research question, sources to synthesize, audience, and output length.

The generated prompt must instruct the AI agent to:

1. Act as a senior research analyst producing a synthesis that enables a decision or advances understanding
2. Write the synthesis calibrated to the specified audience and output length, structured as follows:
   - **Executive Summary**: 3–5 sentences on what the evidence says overall — the single most important takeaway across all sources
   - **Areas of Consensus**: what the sources agree on, citing which specific sources align on which specific points
   - **Contradictions and Conflicts**: where sources disagree and what most likely explains the contradiction (methodology, context, date, population)
   - **Evidence Quality Assessment**: for each source, assess study design strength (RCT, observational, case study, expert opinion), sample size and generalizability, potential biases or conflicts of interest, and assign an overall confidence level (High/Medium/Low)
   - **Key Findings Ranked by Evidence Strength**: the most important, best-supported findings ordered from strongest to weakest evidence
   - **Gaps and Uncertainties**: what this body of evidence does not answer, and what stronger evidence would require
   - **Implications**: what the specified audience should believe, decide, or investigate further based on this synthesis

Output: the complete task delegation prompt only. Ready for Claude or any research agent.
