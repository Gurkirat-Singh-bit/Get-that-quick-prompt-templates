---
id: "before-after-bridge"
title: "Before-After-Bridge: Transformation Narrative Agent Prompt"
description: "Generate a BAB-structured prompt to delegate transformation storytelling to an AI agent — for pitches, landing pages, sales copy, or change communication."
category: "frameworks/creative"
tags: ["bab", "before-after-bridge", "copywriting", "narrative", "agent", "delegation"]
variables:
  - name: "subject"
    label: "Subject (product, idea, or change being pitched)"
    required: true
  - name: "audience"
    label: "Audience (who this is written for)"
    required: true
  - name: "current_state"
    label: "Before (the painful current state)"
    required: true
  - name: "desired_state"
    label: "After (the ideal state after transformation)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a Before-After-Bridge (BAB) copywriting agent prompt. The output will be a task prompt handed to Claude or another writing agent.

Configure it for:
- Subject: {{subject}}
- Audience: {{audience}}
- Current state: {{current_state}}
- Desired state: {{desired_state}}

The generated prompt must instruct the writing agent to:
1. **Before:** Open by immersing {{audience}} in the pain of {{current_state}} — make it visceral and specific, not generic
2. **After:** Paint {{desired_state}} as a concrete, emotionally resonant reality — not features, but how life feels
3. **Bridge:** Explain exactly how {{subject}} bridges the gap — the mechanism, not just the claim. Why does it work?
4. End with a clear CTA

Style requirements to include in the prompt: no jargon, active voice, short paragraphs, first paragraph is the hook.

Output: the complete BAB agent prompt only. The writing agent receiving this should produce finished copy with no further direction. Ready for Claude, GPT, or any writing-capable AI.
