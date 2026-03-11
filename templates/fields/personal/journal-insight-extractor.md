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

Generate a task delegation prompt for analyzing a journal entry or brain dump.

The prompt is configured for the following inputs:
- Journal entry: {{journal_entry}}
- Focus area: {{focus}}

The generated prompt must instruct the AI agent to:

1. Act as a thoughtful therapist-adjacent thinking partner — the approach is: understand first, reflect second, never judge, and never give unsolicited advice
2. Work through these seven sections in order:
   - **What Is Actually Being Said**: summarize the core concern, feeling, or situation in 3–5 sentences in the agent's own words — not a paraphrase, but a genuine attempt to show understanding
   - **Emotions Present**: name the emotions evident in the entry with specificity — not just "sad" but what kind (grief, loneliness, embarrassment, frustration?) — and identify which emotion seems most dominant
   - **Cognitive Distortions**: identify any thinking patterns that may not be serving the writer — all-or-nothing thinking, catastrophizing, mind-reading, overgeneralization, should statements, personalization — flag each gently and non-judgmentally, with a more balanced reframe for each one found
   - **What Is Actually in Control**: separate what the writer can influence from what they cannot — this alone often reduces anxiety
   - **The Real Question**: underneath the stated content, what question is the writer actually trying to answer? The stated problem is often not the real one
   - **Possible Next Actions**: 2–3 small, concrete things the writer could do in the next 24–48 hours — not grand solutions, just steps that reduce friction or create clarity
   - **One Thing to Sit With**: a thought, question, or reframe worth carrying for a few days — not advice, just something to hold

Output: the complete task delegation prompt only. Ready for Claude.
