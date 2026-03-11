---
id: "meeting-prep"
title: "Meeting Prep: Context-Aware Briefing"
description: "Inspired by Satya Nadella's meeting prep prompt — surface what's top of mind for a person before any meeting, using past context and shared history."
category: "fields/business"
tags: ["meeting", "prep", "briefing", "executive", "communication", "nadella", "business"]
variables:
  - name: "person"
    label: "Person You're Meeting (name, role, relationship)"
    required: true
  - name: "meeting_purpose"
    label: "Meeting Purpose (what is the meeting about?)"
    required: true
  - name: "context"
    label: "Context (recent interactions, their priorities, shared history)"
    required: true
  - name: "your_goal"
    label: "Your Goal for This Meeting (what do you want to achieve or decide?)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for preparing a thorough meeting brief.

The prompt is configured for the following inputs:
- Person: {{person}}
- Meeting purpose: {{meeting_purpose}}
- Context: {{context}}
- Your goal: {{your_goal}}

The generated prompt must instruct the AI agent to:

1. Act as a sharp executive coach preparing a concise, actionable meeting brief — inspired by Satya Nadella's approach to meeting preparation
2. Produce a brief with these sections:
   - **Their Likely Priorities**: surface the top 5 things most likely on this person's mind right now based on the context — what they are worried about, optimistic about, or actively trying to accomplish
   - **Common Ground**: identify where your interests and their interests genuinely align and recommend leading from that shared foundation
   - **Potential Friction Points**: name likely areas of disagreement or pushback and suggest a specific way to handle each
   - **Key Questions to Ask**: write 5 open-ended questions designed to build understanding and demonstrate genuine curiosity about their perspective
   - **What to Listen For**: describe 3 specific signals or responses that indicate the meeting is on or off track
   - **Opening 60-Second Framing**: a word-for-word suggested opening that acknowledges their context, establishes shared purpose, and sets a productive tone without over-explaining
   - **Desired Outcome**: define what a successful meeting looks like in concrete terms — what decision, agreement, or understanding should exist when the meeting ends

Output: the complete task delegation prompt only. Ready for Claude.
