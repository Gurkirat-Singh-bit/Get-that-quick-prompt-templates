---
id: "life-audit"
title: "Life Audit: Annual Review Across All Life Domains"
description: "A Reddit-famous annual life audit — score every major life domain, identify misalignments, and design a focused year ahead."
category: "fields/personal"
tags: ["life-audit", "personal", "annual-review", "goals", "self-improvement", "productivity", "reddit"]
variables:
  - name: "year"
    label: "Year Being Reviewed (e.g. 2025)"
    required: true
  - name: "context"
    label: "Major Life Context (brief: where you are, what's been happening)"
    required: true
  - name: "top_priorities"
    label: "Your Top 3 Stated Priorities This Year"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for facilitating an annual life audit.

The prompt is configured for the following inputs:
- Year being reviewed: {{year}}
- Life context: {{context}}
- Top priorities: {{top_priorities}}

The generated prompt must instruct the AI agent to:

1. Act as a thoughtful life coach facilitating a structured, honest annual review — the goal is clarity and a concrete plan, not a feel-good summary
2. Guide a 10-domain scoring exercise — for each domain, prompt the user to provide a score from 1–10, what is working (worth protecting and doing more of), what is not working (friction, dissatisfaction, regret), and what a 9–10 would concretely look like. The 10 domains are: Career & Work, Finances & Wealth, Health & Fitness, Relationships (romantic, family, friendships), Personal Growth & Learning, Fun/Hobbies/Recreation, Physical Environment, Spirituality/Meaning/Purpose, Mental & Emotional Health, and Contribution & Impact
3. Facilitate a year-in-review for the specified year: top 3 wins (be proud of these), top 3 lessons (things that did not go as planned but produced learning), the single most important decision made this year, and one thing to leave behind — one behavior or pattern to stop
4. Produce a misalignment report: compare the stated priorities against where time and energy actually went — be direct and specific about the gap
5. Design the year ahead: identify the 3 domains to focus on (focused energy compounds — not all 10), one keystone habit that would improve multiple domains simultaneously, the single biggest change to make in the next 30 days, and a one-word theme for the year ahead

Output: the complete task delegation prompt only. Ready for Claude or a coaching agent.
