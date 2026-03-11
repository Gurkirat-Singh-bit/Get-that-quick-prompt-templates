---
id: "user-interview-script"
title: "User Interview Script: Research-Ready Question Guide"
description: "Generate a structured user research interview script with warm-up, exploration, and closing phases — using open-ended questions that uncover real behavior."
category: "fields/design"
tags: ["user-research", "interview", "ux", "qualitative", "discovery", "design"]
variables:
  - name: "research_question"
    label: "Research Question (what do you want to learn?)"
    required: true
  - name: "participant_profile"
    label: "Participant Profile (who is being interviewed?)"
    required: true
  - name: "product_context"
    label: "Product or Topic Area"
    required: true
  - name: "duration"
    label: "Interview Duration (e.g. 30 min, 45 min, 60 min)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for creating a complete user research interview script.

The prompt is configured for the following inputs:
- Research question: {{research_question}}
- Participant profile: {{participant_profile}}
- Product context: {{product_context}}
- Interview duration: {{duration}}

The generated prompt must instruct the AI agent to:

1. Act as a senior UX researcher writing a production-ready interview guide
2. Structure the script with time allocations that fit within the specified duration, covering these phases:
   - **Warm-Up**: 3–4 easy, rapport-building questions about the participant's background that have no wrong answers
   - **Current Behavior Exploration**: 5–7 open-ended questions focused on what participants actually do, not what they think or prefer — use "Tell me about the last time you..." framing exclusively; zero product pitching
   - **Pain Points & Motivations**: 4–5 questions digging into frustrations, workarounds, and the underlying "why" — include "What happened next?" and "Why?" as mandatory follow-up probes
   - **Concept Exploration** (if applicable): questions that explore reactions to a concept without leading the witness
   - **Closing**: a "Is there anything you wish I had asked?" wrap-up, permission for follow-up, and a thank-you
3. Add an interviewer notes section at the start covering: how to handle off-topic responses, how to probe without leading, and guidance on using silence productively
4. Append a probing question cheat sheet of 8–10 universal follow-up questions usable at any point in the interview

Output: the complete task delegation prompt only. Ready for Claude or any research-capable agent.
