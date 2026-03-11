---
id: "journal-insight-extractor"
title: "Journal Insight Extractor: Voice Dump → Structured Clarity"
description: "Reddit-famous prompt — dump your thoughts, and get back structured insights: cognitive distortions identified, emotional patterns surfaced, and clear next actions."
category: "fields/personal"
tags: ["journaling", "mental-health", "self-reflection", "clarity", "cognitive-distortions", "reddit", "personal"]
variables:
  - name: "journal_entry"
    label: "Your Brain Dump (write freely — everything on your mind, no filter)"
    required: true
  - name: "focus"
    label: "Focus Area (optional: e.g. anxiety about X, decision about Y, relationship with Z)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are a thoughtful therapist-adjacent thinking partner. Read the following brain dump and help me understand it clearly.

**My Brain Dump:**
{{journal_entry}}

**Focus Area:** {{focus}}

Please do not judge, advise prematurely, or dismiss anything. First understand, then reflect.

## 1. What I'm Actually Saying
Summarize the core concern, feeling, or situation in 3-5 sentences — in your own words, not mine. Help me see if you understood correctly.

## 2. Emotions Present
What emotions are evident in this entry? Name them specifically (not just "sad" — what kind? Grief? Loneliness? Embarrassment? Frustration?). Which seems most dominant?

## 3. Cognitive Distortions (if any)
Identify any thinking patterns that might not be serving me:
- All-or-nothing thinking ("always", "never")
- Catastrophizing (worst-case assumption)
- Mind-reading (assuming what others think)
- Overgeneralization
- Should statements
- Personalization
Flag them gently, not judgmentally. Offer a more balanced reframe for each.

## 4. What's Actually in My Control
Separate what I can influence from what I cannot. This alone often reduces anxiety significantly.

## 5. The Real Question
Underneath all of this, what question am I actually trying to answer? Often the stated problem is not the real one.

## 6. Possible Next Actions
2-3 small, concrete things I could do in the next 24-48 hours. Not grand solutions — just steps that reduce friction or create clarity.

## 7. One Thing to Sit With
A thought, question, or reframe that might be worth carrying for a few days.
