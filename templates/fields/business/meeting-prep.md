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

You are a sharp executive coach. Prepare me for the following meeting.

**Meeting With:** {{person}}
**Purpose:** {{meeting_purpose}}
**Context:** {{context}}
**My Goal:** {{your_goal}}

Produce a meeting brief with:

## 1. Their Likely Priorities (Top 5)
Based on the context provided, what is most likely top of mind for {{person}} right now? What are they worried about, optimistic about, or trying to accomplish?

## 2. Common Ground
Where do your interests and their interests align? Start there.

## 3. Potential Friction Points
Where might you disagree or where might they push back? How should you handle each?

## 4. Key Questions to Ask
5 open-ended questions that will help you understand their perspective and build rapport.

## 5. What to Listen For
3 signals or responses that will tell you whether the meeting is going well or off track.

## 6. Your Opening (First 60 Seconds)
A suggested opening that acknowledges their context, establishes shared purpose, and sets a productive tone.

## 7. Desired Outcome
What does a successful meeting look like? What do you want to walk away with?
