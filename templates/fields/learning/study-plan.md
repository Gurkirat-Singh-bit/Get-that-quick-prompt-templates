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

You are an expert learning designer. Create a personalized study plan.

**Subject:** {{subject}}
**Current Level:** {{current_level}}
**Goal:** {{goal}}
**Available Time:** {{available_time}}
**Timeframe:** {{deadline}}

Produce a structured learning plan:

## 1. Prerequisite Audit
What does someone need to know before starting this? Flag any gaps based on the current level.

## 2. Learning Phases
Break the journey into 3-4 phases (e.g. Foundation → Concepts → Application → Mastery). For each phase:
- What you'll know/be able to do by the end
- Estimated time
- Core topics to cover

## 3. Weekly Schedule
A realistic weekly schedule given {{available_time}}. Specify:
- Concept learning sessions (input)
- Practice/application sessions (output)
- Review/spaced-repetition sessions

## 4. Curated Resources
For each phase, recommend:
- 1-2 books or courses (free and paid options)
- 1 practice resource or project
- 1 community or feedback mechanism

## 5. Milestone Projects
2-3 projects that will make the learning concrete and portfolio-worthy.

## 6. Progress Checkpoints
How to know you're on track. Specific, testable indicators for each phase.
