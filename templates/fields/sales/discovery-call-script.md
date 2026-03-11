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

You are a senior B2B sales coach. Write a complete discovery call script.

**Product:** {{product}}
**Prospect:** {{prospect_profile}}
**Their Likely Pain:** {{likely_pain}}
**Duration:** {{call_duration}}

Structure:

## Pre-Call Research Checklist
5 things to know about the prospect before the call starts.

## Opening (2 min)
- Agenda-setting line that gives them control
- Framing that makes them comfortable sharing honestly
- The one question to never start with

## Company & Context (5 min)
3 questions to understand their business and current state. Avoid anything Google could answer.

## Pain Excavation (SPIN-style) (10 min)
- **Situation questions** (2): Establish current reality
- **Problem questions** (3): Surface explicit or implicit pain related to {{likely_pain}}
- **Implication questions** (3): Help them articulate what the pain *costs* them (time, money, risk)
- **Need-payoff questions** (2): Get them to describe what a solution would be worth

## Qualification (MEDDIC) (5 min)
Questions that surface: Metrics, Economic buyer, Decision criteria, Decision process, Identify champion, Competition.

## Solution Teaser (3 min)
How to introduce your solution *only after* they've articulated their pain — and how to connect it directly to what they just said.

## Next Steps (5 min)
- The ask that advances the deal (not "I'll send you info")
- How to get a follow-up meeting committed before hanging up

## Objection Responses
3 most common objections on this type of call and exactly how to respond to each.
