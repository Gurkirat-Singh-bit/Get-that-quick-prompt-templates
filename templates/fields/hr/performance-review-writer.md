---
id: "performance-review-writer"
title: "Performance Review Writer: Specific, Actionable Feedback"
description: "Write a structured, honest performance review that gives specific evidence, balanced feedback, and a clear development path — not generic platitudes."
category: "fields/hr"
tags: ["hr", "performance-review", "feedback", "manager", "development", "talent"]
variables:
  - name: "employee_role"
    label: "Employee Role and Level"
    required: true
  - name: "review_period"
    label: "Review Period (e.g. H2 2025, Q1 2026)"
    required: true
  - name: "accomplishments"
    label: "Key Accomplishments (specific projects, results, contributions)"
    required: true
  - name: "areas_for_growth"
    label: "Areas for Growth (specific behaviors or gaps observed)"
    required: true
  - name: "goals_next_period"
    label: "Goals for Next Period (what should they focus on?)"
    required: true
  - name: "overall_rating"
    label: "Overall Rating (e.g. Exceeds / Meets / Below expectations)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are an experienced people manager. Write a high-quality performance review.

**Employee Role:** {{employee_role}}
**Review Period:** {{review_period}}
**Overall Rating:** {{overall_rating}}
**Accomplishments:** {{accomplishments}}
**Areas for Growth:** {{areas_for_growth}}
**Goals for Next Period:** {{goals_next_period}}

Guidelines:
- Every claim must be backed by a specific example or observable behavior — no generic statements
- Use the SBI model (Situation → Behavior → Impact) for both positive and constructive feedback
- Avoid hedging language that softens important feedback ("could potentially consider")
- Acknowledge complexity fairly — don't oversimplify performance into just positives or negatives
- The development section should feel like investment, not criticism

Structure:

## Summary
One paragraph capturing the essence of this employee's performance — what defines them this period.

## Strengths & Impact
3-4 specific strengths, each with: the situation, the behavior observed, and the measurable or qualitative impact.

## Areas for Growth
2-3 development areas, each with: what was observed (specific), why it matters, and one concrete action to address it.

## Goals for {{review_period}} — Next Period
3-4 clear, measurable goals for the next review cycle. Each goal should state what, how it will be measured, and by when.

## Overall Assessment
A direct summary paragraph connecting performance to the overall rating and the path forward.
