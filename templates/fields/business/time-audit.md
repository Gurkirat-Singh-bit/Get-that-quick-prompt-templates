---
id: "time-audit"
title: "Time Audit: Calendar & Energy Analysis"
description: "Inspired by Satya Nadella's time allocation prompt — analyze where your time goes, reveal gaps between priorities and actual effort, and redesign your week."
category: "fields/business"
tags: ["time-management", "productivity", "audit", "calendar", "focus", "nadella", "business"]
variables:
  - name: "activities"
    label: "Activities & Time Spent (list your recurring meetings, tasks, and roughly how many hours/week each takes)"
    required: true
  - name: "top_priorities"
    label: "Top 3 Priorities (what matters most for you to succeed right now)"
    required: true
  - name: "timeframe"
    label: "Timeframe (e.g. past 4 weeks, typical week)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for conducting a calendar and time allocation audit.

The prompt is configured for the following inputs:
- Activities and time spent: {{activities}}
- Top priorities: {{top_priorities}}
- Timeframe: {{timeframe}}

The generated prompt must instruct the AI agent to:

1. Act as a strategic productivity coach — inspired by Satya Nadella's time allocation methodology
2. Produce a complete time audit report with these sections:
   - **Time Buckets**: group all activities into 5–7 thematic buckets (e.g. Deep Work, Management/1:1s, Admin, Learning, Low-value meetings) and show the estimated percentage of total time spent in each
   - **Alignment Gap**: compare where time is actually going versus where it should go based on the stated priorities — be direct and specific about misalignments, not diplomatic
   - **Energy Drains**: identify activities consuming time without advancing priorities and categorize each for one of four actions: delete, delegate, batch, or shorten — with a specific recommendation for each
   - **Protected Time Recommendations**: suggest specific time blocks to protect for high-priority deep work — specify which days, duration, and what type of work belongs in each block
   - **Redesigned Week Template**: propose a restructured weekly schedule that better aligns time with priorities — show it as a concrete day-by-day template
   - **One Experiment to Try**: recommend a single specific change to implement this week to test the redesign — small enough to be easy, meaningful enough to produce signal

Output: the complete task delegation prompt only. Ready for Claude.
