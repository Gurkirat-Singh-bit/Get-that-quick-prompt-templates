---
id: "decision-memo"
title: "Decision Memo: Structured Decision Document"
description: "Write a clear, well-reasoned decision memo — state the decision, lay out options, assess tradeoffs, and make a defensible recommendation."
category: "fields/business"
tags: ["decision", "memo", "strategy", "tradeoffs", "recommendation", "business", "leadership"]
variables:
  - name: "decision"
    label: "Decision to Make (what choice needs to be made?)"
    required: true
  - name: "context"
    label: "Context (why is this decision needed now? what triggered it?)"
    required: true
  - name: "options"
    label: "Options Being Considered (list them)"
    required: true
  - name: "decision_criteria"
    label: "Decision Criteria (what factors matter most?)"
    required: true
  - name: "audience"
    label: "Audience (who will read and act on this memo?)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are a strategic advisor. Write a clear, concise decision memo for the following situation.

**Decision:** {{decision}}
**Context:** {{context}}
**Options:** {{options}}
**Decision Criteria:** {{decision_criteria}}
**Audience:** {{audience}}

Structure the memo as follows:

## Decision Required
One sentence: what exactly needs to be decided and by when.

## Background
2-3 paragraphs of context. Why does this decision need to happen now? What happens if it is delayed?

## Options Analysis
For each option:
- **Description:** What does this option actually entail?
- **Pros:** What does it get right?
- **Cons:** What does it sacrifice or risk?
- **Score against criteria:** Rate against each decision criterion (High/Medium/Low)

## Tradeoffs
What are you giving up no matter what you choose? Be honest about the core tension.

## Recommendation
State a clear recommendation. Explain the reasoning in 3-4 sentences. Address the most likely objection directly.

## Next Steps
What needs to happen immediately after the decision is made? List owners and deadlines.
