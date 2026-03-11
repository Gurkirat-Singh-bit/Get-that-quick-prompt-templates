---
id: "race-framework"
title: "RACE Framework: Role, Action, Context, Expectation"
description: "Clarify AI behavior by defining the Role, the specific Action to perform, the Context of the situation, and the Expectation for output quality."
category: "frameworks/structured"
tags: ["race", "framework", "role", "action", "context", "expectation", "intermediate"]
variables:
  - name: "role"
    label: "Role (who is the AI in this scenario?)"
    required: true
  - name: "action"
    label: "Action (what should be done?)"
    required: true
  - name: "context"
    label: "Context (relevant background information)"
    required: true
  - name: "expectation"
    label: "Expectation (what should the output include or achieve?)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

**Role:** You are {{role}}.

**Action:** {{action}}

**Context:** {{context}}

**Expectation:** {{expectation}}

Using the context provided, perform the specified action in your assigned role. Ensure your response fully meets the stated expectation.
