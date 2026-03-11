---
id: "launch-readiness"
title: "Launch Readiness: Risk Assessment & Go/No-Go"
description: "Inspired by Satya Nadella's launch tracking prompt — assess launch readiness, surface risks, and produce a probability-based go/no-go recommendation."
category: "fields/product"
tags: ["launch", "readiness", "risk", "go-no-go", "product", "planning", "nadella"]
variables:
  - name: "product_name"
    label: "Product / Feature Name"
    required: true
  - name: "launch_date"
    label: "Target Launch Date"
    required: true
  - name: "current_status"
    label: "Current Status (what's done, what's in progress, what's blocked)"
    required: true
  - name: "success_criteria"
    label: "Launch Success Criteria (what must be true to ship)"
    required: true
  - name: "known_risks"
    label: "Known Risks (issues already flagged)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for conducting a launch readiness assessment.

The prompt is configured for the following inputs:
- Product: {{product_name}}
- Launch date: {{launch_date}}
- Current status: {{current_status}}
- Success criteria: {{success_criteria}}
- Known risks: {{known_risks}}

The generated prompt must instruct the AI agent to:

1. Act as a senior product manager running a launch readiness review
2. Assess readiness across five areas — engineering completion (feature completeness, open bug backlog), QA and testing (coverage, open P0/P1 issues), rollout infrastructure (feature flags, monitoring, rollback plan), documentation and support readiness, and marketing and communications readiness
3. Produce a risk register for all identified risks, with each entry scored by likelihood (High/Medium/Low), impact if it occurs (Critical/Significant/Minor), and a specific mitigation action
4. Give an honest launch probability estimate (0–100%) with clear reasoning on what factors are driving the number up or down
5. Make a single unambiguous recommendation: GO, GO WITH CONDITIONS, or NO-GO — if conditional or negative, list the exact blockers and the deadline by which each must be resolved
6. Close with a numbered action item list covering the next 48–72 hours, with a named owner and deadline for each item

Output: the complete task delegation prompt only. Ready to paste into Claude.
