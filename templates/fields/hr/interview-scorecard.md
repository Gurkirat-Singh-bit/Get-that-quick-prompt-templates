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

You are a talent acquisition expert. Build a structured interview scorecard for the following role.

**Role:** {{role}}
**Seniority:** {{seniority}}
**Key Competencies:** {{key_competencies}}
**Duration:** {{interview_duration}}

Produce a complete interview guide:

## Interview Structure
Time allocation across competency areas that fits within {{interview_duration}}.

## Competency Scorecard
For each competency listed, provide:

**[Competency Name]**
- *Why it matters for this role* (1 sentence)
- *Behavioral question* (STAR-format trigger: "Tell me about a time when...")
- *Follow-up probes* (2-3 questions to go deeper if answer is vague)
- *Green flags* (what strong answers look like)
- *Red flags* (warning signs in weak answers)
- *Scoring rubric* (1=Poor / 2=Below expectations / 3=Meets / 4=Exceeds / 5=Exceptional — describe each)

## Culture & Values Questions
2-3 questions to assess alignment with typical team culture.

## Candidate Questions Section
Space for the interviewer to note the quality of questions the candidate asks.

## Overall Scorecard Template
A summary table: competency → score (1-5) → evidence (brief notes) → hire recommendation.

## Decision Framework
What score threshold = strong hire / hire / no hire? How to handle split decisions across a panel.
