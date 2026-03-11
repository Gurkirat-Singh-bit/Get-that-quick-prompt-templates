---
id: "perspective-shift"
title: "Perspective Shift: Multi-Viewpoint Analysis Agent Prompt"
description: "Generate a prompt to delegate multi-stakeholder analysis to an AI agent — surfaces hidden conflicts, alignments, and blind spots across viewpoints."
category: "frameworks/creative"
tags: ["perspective", "analysis", "stakeholders", "agent", "delegation", "decision-making"]
variables:
  - name: "topic"
    label: "Topic or Decision to Analyze"
    required: true
  - name: "perspectives"
    label: "Perspectives to Include (list 3-5 stakeholders or viewpoints)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a multi-perspective analysis agent prompt. This will be given to Claude or another AI to produce a structured stakeholder analysis.

Configure it for:
- Topic: {{topic}}
- Perspectives: {{perspectives}}

The generated prompt must instruct the agent to:
1. Analyze {{topic}} through each of these lenses: {{perspectives}}
2. For each perspective: interests, how they view the topic, what they gain/lose, key concerns, what they'd recommend
3. After all perspectives: identify where they align, where they conflict, and what blind spots no single perspective captures
4. Produce a synthesis recommendation that integrates the key insights across all viewpoints

The agent must approach each perspective with genuine empathy — no strawmanning, no picking a winner before the analysis is done.

Output: the complete analysis agent prompt only. Ready to hand to Claude, GPT, or any AI agent capable of nuanced multi-stakeholder reasoning.
