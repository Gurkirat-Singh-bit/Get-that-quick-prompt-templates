---
id: "study-plan"
title: "Study Plan: Structured Learning Curriculum"
description: "Create a personalized, spaced-repetition-aware study plan for any skill or subject — with milestones, resources, and practice exercises."
category: "fields/learning"
tags: ["study-plan", "learning", "curriculum", "skills", "education", "self-improvement"]
variables:
  - name: "subject"
    label: "Subject or Skill to Learn"
    required: true
  - name: "current_level"
    label: "Current Level (complete beginner / have some basics / intermediate)"
    required: true
  - name: "goal"
    label: "Learning Goal (what should you be able to DO after this?)"
    required: true
  - name: "available_time"
    label: "Available Time (e.g. 1 hour/day, weekends only, 10 hours/week)"
    required: true
  - name: "deadline"
    label: "Deadline or Timeframe (e.g. 3 months, 6 weeks, no deadline)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for creating a personalized study plan.

The prompt is configured for the following inputs:
- Subject: {{subject}}
- Current level: {{current_level}}
- Goal: {{goal}}
- Available time: {{available_time}}
- Deadline: {{deadline}}

The generated prompt must instruct the AI agent to:

1. Act as an expert learning designer creating a plan that balances structure with realistic time constraints
2. Produce a complete study plan with these sections:
   - **Prerequisite Audit**: what needs to be in place before starting, with specific gaps to address based on the current level
   - **Learning Phases**: 3–4 phases (e.g. Foundation, Concepts, Application, Mastery) — for each: what the learner will know or be able to do at the end, estimated time, and core topics to cover
   - **Weekly Schedule**: a realistic schedule built around the available time — specifying concept learning sessions (input), practice and application sessions (output), and review/spaced-repetition sessions
   - **Curated Resources**: for each phase, recommend 1–2 books or courses (include both free and paid options), one practice resource or project, and one community or feedback mechanism
   - **Milestone Projects**: 2–3 projects that make the learning concrete and produce something demonstrable
   - **Progress Checkpoints**: specific, testable indicators for each phase so the learner can self-assess without guessing

Output: the complete task delegation prompt only. Ready for Claude or a learning-design agent.
