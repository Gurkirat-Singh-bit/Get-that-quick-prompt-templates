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

You are a senior product manager running launch readiness for **{{product_name}}**, targeting **{{launch_date}}**.

**Current Status:** {{current_status}}

**Launch Success Criteria:** {{success_criteria}}

**Known Risks:** {{known_risks}}

Produce a full launch readiness report:

## 1. Status Assessment
Evaluate progress across:
- Engineering completion (feature completeness, bug backlog)
- QA & testing (coverage, open P0/P1 bugs)
- Rollout infrastructure (feature flags, monitoring, rollback plan)
- Documentation & support readiness
- Marketing & communications readiness

## 2. Risk Register
For each risk, assess:
- **Likelihood:** High / Medium / Low
- **Impact if it occurs:** Critical / Significant / Minor
- **Mitigation:** What can be done before launch?

## 3. Launch Probability
Give an honest probability estimate (0-100%) that the launch will be successful by {{launch_date}}. Explain the key factors driving this number up or down.

## 4. Go / No-Go Recommendation
State a clear recommendation: **GO**, **GO WITH CONDITIONS**, or **NO-GO**.
If conditional or no-go, list the exact blockers that must be resolved and by when.

## 5. Action Items
Numbered list of owners, actions, and deadlines for the next 48-72 hours.
