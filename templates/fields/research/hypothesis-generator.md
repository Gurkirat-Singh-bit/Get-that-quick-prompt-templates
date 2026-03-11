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

You are an experienced research scientist. Generate a set of testable hypotheses for the following.

**Phenomenon:** {{phenomenon}}
**Field:** {{field}}
**Existing Knowledge:** {{existing_knowledge}}
**Constraints:** {{constraints}}

Produce 6-8 distinct hypotheses:

For each hypothesis:

**Hypothesis [N]: [Short Name]**
- **Statement:** A clear, falsifiable hypothesis in the form "If [X], then [Y], because [mechanism]"
- **Rationale:** Why this is a plausible explanation based on existing theory or observation
- **Testability Score:** 1-5 (1=nearly impossible, 5=straightforward to test)
- **Null Hypothesis:** The corresponding H₀
- **Suggested Methodology:** The most appropriate research design (experiment, survey, longitudinal study, natural experiment, etc.)
- **Key Variables:** What to measure, what to control
- **Potential Confounders:** What could muddy the results
- **Time & Resource Estimate:** Rough feasibility given {{constraints}}

---

## Prioritization
Rank the hypotheses by: (novelty × feasibility × potential impact). Recommend the top 2 to pursue first and explain why.
