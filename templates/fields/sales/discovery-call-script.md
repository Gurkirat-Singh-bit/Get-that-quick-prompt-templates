---
id: "discovery-call-script"
title: "Discovery Call Script: Qualification & Pain Excavation"
description: "A structured discovery call framework that qualifies prospects, uncovers real pain, and sets up a compelling follow-up — without feeling like an interrogation."
category: "fields/sales"
tags: ["sales", "discovery", "b2b", "qualification", "call-script", "MEDDIC", "SPIN"]
variables:
  - name: "product"
    label: "Your Product / Service"
    required: true
  - name: "prospect_profile"
    label: "Prospect Profile (role, company type, industry)"
    required: true
  - name: "likely_pain"
    label: "Likely Pain Points (problems your product solves)"
    required: true
  - name: "call_duration"
    label: "Call Duration (e.g. 30 min)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for creating a complete discovery call script.

The prompt is configured for the following inputs:
- Product: {{product}}
- Prospect profile: {{prospect_profile}}
- Likely pain: {{likely_pain}}
- Call duration: {{call_duration}}

The generated prompt must instruct the AI agent to:

1. Act as a senior B2B sales coach writing a script that uncovers real pain and qualifies the opportunity without feeling like an interrogation
2. Write a pre-call research checklist of 5 specific things to know about the prospect before the call starts
3. Write the call opening: an agenda-setting line that gives the prospect control, framing that makes honest sharing comfortable, and one question to never open with (and why)
4. Write company and context questions (3) that cannot be answered by a Google search
5. Write a full SPIN-style pain excavation sequence: 2 Situation questions (establish current reality), 3 Problem questions (surface explicit or implicit pain tied to the likely pain points), 3 Implication questions (help them articulate what the pain costs them in time, money, or risk), and 2 Need-payoff questions (get them to describe what solving it would be worth)
6. Write MEDDIC qualification questions covering: Metrics, Economic buyer, Decision criteria, Decision process, Champion identification, and Competition
7. Write a solution teaser that only appears after they have articulated their pain — including how to connect it directly to what they just said
8. Write the next steps close: the ask that advances the deal and how to get a follow-up commitment before hanging up
9. Write responses to the 3 most common objections on this type of call — word for word

Output: the complete task delegation prompt only. Ready for Claude or a sales coaching agent.
