---
id: "1on1-prep"
title: "1-on-1 Meeting Prep: Manager & Report Agenda"
description: "Prepare a structured 1-on-1 agenda with the right balance of updates, blockers, development, and relationship-building — for managers or direct reports."
category: "fields/hr"
tags: ["1on1", "manager", "meeting", "hr", "leadership", "team", "feedback"]
variables:
  - name: "your_role"
    label: "Your Role (manager or direct report?)"
    required: true
  - name: "other_person"
    label: "Other Person's Role and Context"
    required: true
  - name: "recent_context"
    label: "Recent Context (what's happened since the last 1-on-1?)"
    required: true
  - name: "duration"
    label: "Duration (e.g. 30 min, 45 min)"
    required: false
  - name: "relationship_stage"
    label: "Relationship Stage (new, established, tense, thriving)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for preparing a 1-on-1 meeting.

The prompt is configured for the following variables: your role (manager or direct report), the other person's role and context, recent context since the last 1-on-1, meeting duration, and relationship stage.

The generated prompt must instruct the AI agent to:

1. Act as an executive coach preparing a complete, ready-to-use 1-on-1 brief
2. Build a time-blocked agenda for the specified duration that puts their agenda first — their updates and what is on their mind come before the manager's topics
3. Write an opening question that builds psychological safety and gets honest conversation started rather than a status report
4. For any feedback to give: write it out word-for-word in Situation → Behavior → Impact format so it can be delivered without fumbling
5. Prepare 3–4 questions designed to surface what the other person is not volunteering — what they are thinking, feeling, or struggling with that would not come up unprompted
6. If the recent context or relationship stage suggests any tension or difficult topic: prepare a word-for-word opening line, a listening strategy for when they respond, and a close that leaves the conversation productive rather than unresolved
7. Include a documentation template for the end of the meeting: commitments made, by whom, and by when

Output: the complete task delegation prompt only. Ready for Claude.
