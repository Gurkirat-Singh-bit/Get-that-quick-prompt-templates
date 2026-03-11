---
id: "socratic-debate"
title: "Socratic Debate: Challenge Your Assumptions"
description: "Use Socratic questioning to stress-test an idea, plan, or belief — surface hidden assumptions and sharpen your thinking."
category: "fields/learning"
tags: ["socratic", "debate", "critical-thinking", "assumptions", "philosophy", "learning", "reasoning"]
variables:
  - name: "claim"
    label: "Claim or Belief (the idea you want to stress-test)"
    required: true
  - name: "context"
    label: "Context (why you hold this belief or plan)"
    required: false
  - name: "depth"
    label: "Depth of Challenge (gentle / moderate / ruthless)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for Socratic stress-testing of a claim or belief.

The prompt is configured for the following inputs:
- Claim: {{claim}}
- Context: {{context}}
- Depth of challenge: {{depth}}

The generated prompt must instruct the AI agent to:

1. Act as a Socratic philosopher and rigorous thinker — the goal is to strengthen the thinking, not to win an argument or be contrarian
2. Work through exactly 6 rounds in sequence:
   - **Round 1 — Clarification**: ask 3 questions that force the claim to be stated more precisely — what exactly is being claimed, and what do the key terms actually mean?
   - **Round 2 — Probing Assumptions**: identify 3–4 hidden assumptions the claim depends on — for each, ask what happens if that assumption is wrong
   - **Round 3 — Challenging Evidence**: what evidence would be needed to prove this claim? What evidence could disprove it? Is the current evidence actually sufficient, or is the claim over-extended?
   - **Round 4 — Counterexamples**: generate 2–3 specific cases where the claim breaks down — determine whether these are edge cases or fundamental problems
   - **Round 5 — Steelmanning**: present the strongest possible version of the argument for the original claim — take it seriously and do not straw-man it
   - **Round 6 — Synthesis**: what survives this process? What needs to be modified? What should be discarded? Produce a refined, more defensible version of the original claim
3. Calibrate the intensity of each round to match the specified depth of challenge

Output: the complete task delegation prompt only. Ready for Claude or any reasoning agent.
