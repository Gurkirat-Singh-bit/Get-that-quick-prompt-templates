---
id: "sales-proposal"
title: "Sales Proposal: Value-Led, Deal-Closing Document"
description: "Write a compelling sales proposal that leads with the prospect's problem, quantifies your value, and makes it easy to say yes."
category: "fields/sales"
tags: ["sales", "proposal", "b2b", "closing", "ROI", "business-case", "deal"]
variables:
  - name: "prospect_name"
    label: "Prospect / Company Name"
    required: true
  - name: "their_problem"
    label: "Their Problem (in their words if possible)"
    required: true
  - name: "your_solution"
    label: "Your Proposed Solution (specific scope)"
    required: true
  - name: "pricing"
    label: "Pricing (what you're proposing)"
    required: true
  - name: "timeline"
    label: "Timeline (start date, implementation, key milestones)"
    required: true
  - name: "success_metrics"
    label: "Success Metrics (how you'll both know it worked)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for writing a sales proposal.

The prompt is configured for the following inputs:
- Prospect name: {{prospect_name}}
- Their problem: {{their_problem}}
- Your solution: {{your_solution}}
- Pricing: {{pricing}}
- Timeline: {{timeline}}
- Success metrics: {{success_metrics}}

The generated prompt must instruct the AI agent to:

1. Act as a senior enterprise account executive writing a proposal designed to close — not just to inform
2. Write a proposal with this exact structure:
   - **Executive Summary**: 2 paragraphs — mirror back the prospect's problem in their own language, then state the solution and the expected outcome; this section alone must be shareable to an executive who will not read the rest
   - **The Problem We're Solving Together**: articulate their current state, the cost of inaction, and the consequences they have described — make them feel deeply understood before anything is pitched
   - **Our Proposed Solution**: exactly what is being delivered, how, and in what sequence — no vague capabilities, only concrete deliverables
   - **The ROI Case**: quantify the expected impact in the prospect's terms — time saved multiplied by cost, revenue upside, risk reduction value, and comparison to the cost of the status quo
   - **Investment**: present the pricing as an investment against the ROI calculated above, not as a line-item cost
   - **Implementation Timeline**: key milestones, who owns what, and what success looks like at each stage
   - **Success Criteria**: the specific metrics that will be used to measure outcomes, agreed upfront
   - **Why Us**: exactly 3 reasons specific to this deal — not a generic company pitch
   - **Next Steps**: one clear action — what they sign, what happens next, and what their team needs to do to begin

Output: the complete task delegation prompt only. Ready for Claude or a sales writing agent.
