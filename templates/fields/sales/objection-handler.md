---
id: "objection-handler"
title: "Objection Handler: Acknowledge, Reframe & Advance"
description: "Prepare confident, non-pushy responses to the most common sales objections — using the ARA method: Acknowledge, Reframe, Advance."
category: "fields/sales"
tags: ["sales", "objections", "b2b", "negotiation", "closing", "script"]
variables:
  - name: "product"
    label: "Your Product / Service"
    required: true
  - name: "price_point"
    label: "Price Point (rough pricing to calibrate objections)"
    required: false
  - name: "typical_customer"
    label: "Typical Customer (role and company type)"
    required: true
  - name: "objections"
    label: "Specific Objections to Prepare For (or leave blank for common ones)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for scripting objection responses.

The prompt is configured for the following inputs:
- Product: {{product}}
- Price point: {{price_point}}
- Typical customer: {{typical_customer}}
- Specific objections: {{objections}}

The generated prompt must instruct the AI agent to:

1. Act as a veteran B2B sales trainer writing word-for-word response scripts — the goal is confident, non-pushy responses that advance the sale
2. Apply the ARA method to every objection: Acknowledge (validate the concern without agreeing or caving), Reframe (shift the frame without dismissing the point), Advance (move the conversation toward a decision)
3. Prepare complete entries for the following objections — plus any additional ones specified in the variables:
   - "It's too expensive / we don't have budget": ARA response word-for-word, the question to ask to uncover the real concern, and what NOT to say
   - "We already have a solution for this": ARA response, how to explore switching cost and dissatisfaction, and when to walk away vs. persist
   - "Now isn't a good time": ARA response, how to distinguish real timing from avoidance, and how to stay warm without being annoying
   - "I need to think about it / talk to my team": ARA response, how to uncover the real blocker, and a close that creates momentum without pressure
   - "Send me some information and I'll get back to you": ARA response (this is usually a polite no), how to distinguish genuine interest from a brushoff, and what to send with what follow-up to agree on
4. For every entry: write out the exact words to say and include a note on tone and delivery

Output: the complete task delegation prompt only. Ready for Claude or a sales training agent.
