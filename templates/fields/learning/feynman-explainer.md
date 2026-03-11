---
id: "feynman-explainer"
title: "Feynman Explainer: Teach It Simply to Learn It Deeply"
description: "Apply the Feynman Technique — explain any concept from first principles as simply as possible, expose gaps, and rebuild with clarity."
category: "fields/learning"
tags: ["feynman", "learning", "teaching", "simplification", "first-principles", "education"]
variables:
  - name: "concept"
    label: "Concept to Explain (any topic, field, or idea)"
    required: true
  - name: "audience"
    label: "Audience (e.g. a curious 10-year-old, a non-technical executive, a first-year student)"
    required: true
  - name: "depth"
    label: "Depth Required (overview / intermediate / deep dive)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for producing a Feynman-style explanation of a concept.

The prompt is configured for the following inputs:
- Concept: {{concept}}
- Audience: {{audience}}
- Depth: {{depth}}

The generated prompt must instruct the AI agent to:

1. Act as a world-class teacher applying the Feynman Technique — the goal is genuine understanding, not the appearance of it
2. Work through all 6 steps of the technique in order:
   - **Step 1 — Simple Explanation**: explain the concept as if the audience has never encountered it, using plain language with zero jargon — if a technical term is unavoidable, define it immediately in one plain sentence
   - **Step 2 — Core Analogy**: find one analogy from everyday life that captures the essence of the concept, explain how the analogy maps to reality, and explicitly state where the analogy breaks down
   - **Step 3 — Worked Example**: walk through one concrete, specific example demonstrating the concept in action — show the input and output, or before and after
   - **Step 4 — Common Misconceptions**: identify 2–3 things most people misunderstand or oversimplify about this concept and explain what the correct understanding looks like
   - **Step 5 — First-Principles Rebuild**: reconstruct the explanation using only what the audience already understands — no appeals to authority, derive it from foundational ideas
   - **Step 6 — One-Sentence Definition**: write a single sentence that captures the complete idea accurately — simple but not simplistic
3. If the explanation reveals a genuine gap in the available knowledge, flag it explicitly rather than papering over it

Output: the complete task delegation prompt only. Ready for Claude, GPT, or any explanatory AI agent.
