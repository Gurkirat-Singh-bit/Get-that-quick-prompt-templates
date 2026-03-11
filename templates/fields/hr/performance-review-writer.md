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

Generate a task delegation prompt for writing a high-quality performance review.

The prompt is configured for the following variables: employee role and level, review period, key accomplishments, areas for growth, goals for next period, and overall rating.

The generated prompt must instruct the AI agent to:

1. Act as an experienced people manager writing a review that is honest, fair, and development-oriented
2. Apply the SBI model (Situation → Behavior → Impact) to every piece of feedback — both positive and constructive — with no generic statements and no claims without a specific observable example
3. Avoid hedging language that softens important messages (e.g. "could potentially consider") — say what needs to be said directly
4. Write the development section so it feels like investment in the person, not criticism of them
5. Use this exact structure:
   - **Summary**: one paragraph capturing the essence of this employee's performance and what defines them this period
   - **Strengths & Impact**: 3–4 specific strengths, each with the Situation, the Behavior observed, and the measurable or qualitative Impact
   - **Areas for Growth**: 2–3 development areas, each with what was specifically observed, why it matters, and one concrete action to address it
   - **Goals for Next Period**: 3–4 clear, measurable goals — each stating what the goal is, how it will be measured, and by when
   - **Overall Assessment**: a direct paragraph connecting performance to the overall rating and describing the path forward

Output: the complete task delegation prompt only. Ready for Claude.
