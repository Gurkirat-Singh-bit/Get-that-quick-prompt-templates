---
id: "interview-scorecard"
title: "Interview Scorecard: Competency-Based Question Guide"
description: "Generate a structured interview scorecard with behavioral questions, follow-up probes, and evaluation criteria for any role."
category: "fields/hr"
tags: ["interview", "hiring", "scorecard", "competency", "behavioral", "hr", "recruiting"]
variables:
  - name: "role"
    label: "Role Being Hired For"
    required: true
  - name: "key_competencies"
    label: "Key Competencies to Evaluate (e.g. communication, problem-solving, leadership, technical skill)"
    required: true
  - name: "seniority"
    label: "Seniority Level (junior / mid / senior / lead / executive)"
    required: true
  - name: "interview_duration"
    label: "Interview Duration (e.g. 45 min)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for creating a structured interview scorecard.

The prompt is configured for the following variables: role being hired for, key competencies to evaluate, seniority level, and interview duration.

The generated prompt must instruct the AI agent to:

1. Act as a talent acquisition expert building a guide that produces consistent, evidence-based hiring decisions
2. Produce a time-blocked interview structure that fits within the specified duration and allocates time proportionally across competencies
3. For each competency, produce a complete entry:
   - Why it matters for this role (1 sentence)
   - A behavioral STAR question ("Tell me about a time when...")
   - 2–3 follow-up probes to go deeper when answers are vague
   - Green flags describing what strong answers look like
   - Red flags describing what weak or concerning answers signal
   - A 1–5 scoring rubric with a description for each level (1=Poor through 5=Exceptional)
4. Add 2–3 culture and values questions calibrated to the seniority level
5. Include a candidate questions quality section — a guide for the interviewer on how to evaluate the questions the candidate asks
6. Produce a summary scorecard template: competency, score (1–5), evidence notes, and hire recommendation
7. Define decision thresholds: what score combination equals a strong hire, hire, and no-hire, and how to handle split decisions in a panel

Output: the complete task delegation prompt only. Ready for Claude or an HR agent.
