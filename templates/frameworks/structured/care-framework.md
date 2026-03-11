---
id: "care-framework"
title: "CARE Framework: Context, Action, Result, Example"
description: "Achieve high-precision outputs by establishing Context, defining the Action, specifying the Result needed, and grounding it with an Example."
category: "frameworks/structured"
tags: ["care", "framework", "context", "action", "result", "example", "intermediate"]
variables:
  - name: "context"
    label: "Context (situation or background)"
    required: true
  - name: "action"
    label: "Action (what needs to be performed)"
    required: true
  - name: "result"
    label: "Result (what the output should achieve)"
    required: true
  - name: "example"
    label: "Example (sample, reference, or similar output to model after)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

**Context:** {{context}}

**Action:** {{action}}

**Result:** The output should: {{result}}

**Example:** {{example}}

Using the context and example as a guide, perform the action and produce a result that matches the specified outcome.
