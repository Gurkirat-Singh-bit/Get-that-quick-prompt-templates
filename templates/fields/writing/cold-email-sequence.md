---
id: "cold-email-sequence"
title: "Cold Email Sequence: Research-Personalized Outreach"
description: "Write a 3-touch cold email sequence that leads with value, builds trust, and earns a reply — without being pushy."
category: "fields/writing"
tags: ["cold-email", "outreach", "sales", "copywriting", "email", "writing", "marketing"]
variables:
  - name: "sender_role"
    label: "Your Role / Product (who are you and what do you offer?)"
    required: true
  - name: "recipient_profile"
    label: "Recipient Profile (role, company type, likely pain points)"
    required: true
  - name: "value_proposition"
    label: "Value Proposition (one specific, concrete outcome you deliver)"
    required: true
  - name: "proof"
    label: "Social Proof (customer name, stat, or result you can reference)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for writing a 3-touch cold email sequence.

The prompt is configured for the following inputs:
- Sender: {{sender_role}}
- Recipient: {{recipient_profile}}
- Value proposition: {{value_proposition}}
- Proof: {{proof}}

The generated prompt must instruct the AI agent to:

1. Act as an expert B2B copywriter who writes email sequences that earn replies without being pushy
2. Write a 3-email sequence with the following structure:
   - **Email 1 — Value-First Introduction (Day 1)**: specific subject line that references their situation (no clickbait), one-sentence opening that shows genuine research, body connecting a concrete problem they likely face to the value proposition using the proof point, one low-friction CTA (a yes/no question, not "jump on a call"), under 100 words
   - **Email 2 — Different Angle (Day 4)**: new subject line, different opening approach, lead with a relevant insight or data point for their role or industry, connect it to the value proposition, slightly warmer CTA, under 100 words
   - **Email 3 — Graceful Breakup (Day 9)**: subject line that creates a response paradox (e.g. "Should I close your file?"), acknowledge prior outreach without guilt-tripping, one-sentence final value statement, an easy opt-out that paradoxically increases response rate, under 50 words
3. After each email, include a brief note explaining the psychological or strategic reason the approach works

Output: the complete task delegation prompt only. Ready for Claude or a copywriting agent.
