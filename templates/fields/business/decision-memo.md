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

Generate a task delegation prompt for writing a structured decision memo.

The prompt is configured for the following inputs:
- Decision: {{decision}}
- Context: {{context}}
- Options: {{options}}
- Decision criteria: {{decision_criteria}}
- Audience: {{audience}}

The generated prompt must instruct the AI agent to:

1. Act as a strategic advisor writing a memo that enables a clear, documented decision
2. Write a structured memo with these sections — every section must be specific and concrete, no filler:
   - **Decision Required**: one sentence stating exactly what needs to be decided and by when
   - **Background**: why this decision is needed now and what the cost of delay is (2–3 paragraphs)
   - **Options Analysis**: for each option — what it actually entails, pros, cons, and a score against each decision criterion (High/Medium/Low)
   - **Tradeoffs**: what is given up no matter which option is chosen — be honest about the core tension that no option fully resolves
   - **Recommendation**: a clear stated recommendation with 3–4 sentences of reasoning and a direct pre-emption of the most likely objection
   - **Next Steps**: what happens immediately after the decision is made, with named owners and deadlines
3. Write for the specified audience — calibrate the level of detail and framing accordingly
4. Keep the memo to a length that can be read in under 5 minutes

Output: the complete task delegation prompt only. Ready for Claude.
