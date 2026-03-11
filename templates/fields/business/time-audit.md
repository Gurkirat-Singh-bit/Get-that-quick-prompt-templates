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

You are a strategic productivity coach. Analyze the following time allocation.

**Activities and Time:**
{{activities}}

**Top Priorities:**
{{top_priorities}}

**Timeframe:** {{timeframe}}

Produce a time audit report:

## 1. Time Buckets
Group all activities into 5-7 thematic buckets (e.g. "Deep Work", "Management/1:1s", "Admin", "Learning", "Meetings with no clear outcome"). Show the estimated % of time in each.

## 2. Alignment Gap
Compare where time is actually going vs. where it should go based on the top priorities. Be blunt about misalignments.

## 3. Energy Drains
Identify activities that are consuming time but not advancing priorities. Flag meetings or tasks that could be: deleted, delegated, batched, or shortened.

## 4. Protected Time Recommendations
Suggest specific time blocks to protect for high-priority deep work. Be specific — which days, how long, what type of work.

## 5. Redesigned Week Template
Propose a restructured weekly template that better aligns time with priorities. Show it as a simple schedule.

## 6. One Experiment to Try
Recommend one specific change to make this week to test the new approach.
