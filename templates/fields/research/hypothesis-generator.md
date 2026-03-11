---
id: "hypothesis-generator"
title: "Hypothesis Generator: Research Hypotheses with Testability Scores"
description: "Generate a set of ranked research hypotheses for any phenomenon — each with a rationale, testability assessment, and suggested methodology."
category: "fields/research"
tags: ["research", "hypothesis", "scientific-method", "academic", "experiment", "methodology"]
variables:
  - name: "phenomenon"
    label: "Phenomenon or Observation to Explain"
    required: true
  - name: "field"
    label: "Research Field"
    required: true
  - name: "existing_knowledge"
    label: "Existing Knowledge (what is already known or established?)"
    required: false
  - name: "constraints"
    label: "Research Constraints (budget, time, access, ethical limits)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for generating a set of research hypotheses.

The prompt is configured for the following variables: phenomenon to explain, research field, existing knowledge, and research constraints.

The generated prompt must instruct the AI agent to:

1. Act as an experienced research scientist generating hypotheses that are genuinely novel and testable — not obvious restatements of existing knowledge
2. Generate 6–8 distinct hypotheses, with each one formulated as a falsifiable statement in the form "If X, then Y, because Z (mechanism)"
3. For each hypothesis, produce a complete entry with:
   - The falsifiable statement in the required format
   - A rationale explaining why this is a plausible explanation based on existing theory or observation
   - A testability score from 1–5 (1 = nearly impossible to test, 5 = straightforward)
   - The corresponding null hypothesis
   - The most appropriate suggested methodology (experiment, survey, longitudinal study, natural experiment, etc.)
   - Key variables to measure and control
   - Potential confounders that could muddy the results
   - A rough time and resource feasibility estimate given the stated constraints
4. Close with a prioritization: rank all hypotheses by (novelty × feasibility × potential impact) and recommend the top 2 to pursue first, with a clear explanation of why

Output: the complete task delegation prompt only. Ready for Claude or a scientific research agent.
