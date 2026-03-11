---
id: "co-star-framework"
title: "CO-STAR Framework: Context, Objective, Style, Tone, Audience, Response"
description: "Generate a CO-STAR-structured prompt for delegating polished, audience-calibrated content work to AI agents."
category: "frameworks/advanced"
tags: ["co-star", "costar", "framework", "prompt-generation", "content", "communications", "agent"]
variables:
  - name: "context"
    label: "Context (background, industry, situation)"
    required: true
  - name: "objective"
    label: "Objective (what this content must accomplish)"
    required: true
  - name: "style"
    label: "Style (writing style: formal, conversational, technical, narrative)"
    required: true
  - name: "tone"
    label: "Tone (emotional quality: authoritative, friendly, urgent, empathetic)"
    required: true
  - name: "audience"
    label: "Audience (who reads this — role, knowledge level, what they care about)"
    required: true
  - name: "response_format"
    label: "Response Format (how the output must be structured)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a fully configured content agent prompt using the CO-STAR framework. This will be handed to an AI agent (Claude, GPT, Gemini) to produce polished, audience-calibrated content.

Build each dimension into the prompt:
- **C — Context:** Ground the agent in "{{context}}" — industry, situation, what exists already.
- **O — Objective:** Give the agent "{{objective}}" as its purpose — what must be true after the content is read.
- **S — Style:** Enforce "{{style}}" — link it to specific writing patterns the agent must follow.
- **T — Tone:** Mandate "{{tone}}" — describe what it sounds like and what it must never sound like.
- **A — Audience:** Define "{{audience}}" in detail — their role, knowledge level, biases, and what they respond to.
- **R — Response:** Specify "{{response_format}}" exactly — sections, length, structure.

Output: the complete CO-STAR agent prompt only. Every element configured so the agent produces content that fits perfectly without iteration. Ready to paste into any AI content workflow.
