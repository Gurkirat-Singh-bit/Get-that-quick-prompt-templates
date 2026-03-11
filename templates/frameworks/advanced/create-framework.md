---
id: "create-framework"
title: "CREATE Framework: Character, Request, Examples, Adjustments, Type, Extras"
description: "A detailed 6-part framework for complex projects — assign a Character, make a Request, provide Examples, specify Adjustments, define the output Type, and add Extras."
category: "frameworks/advanced"
tags: ["create", "framework", "character", "request", "examples", "adjustments", "type", "extras", "advanced"]
variables:
  - name: "character"
    label: "Character (AI persona/role with specific expertise)"
    required: true
  - name: "request"
    label: "Request (what you need produced or accomplished)"
    required: true
  - name: "examples"
    label: "Examples (reference samples, demonstrations, or prior work to model)"
    required: false
  - name: "adjustments"
    label: "Adjustments (specific refinements, constraints, or modifications)"
    required: true
  - name: "output_type"
    label: "Type (output type: essay, code, bullet list, email, report, etc.)"
    required: true
  - name: "extras"
    label: "Extras (any additional requirements or special instructions)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

**Character:** You are {{character}}.

**Request:** {{request}}

**Examples:** Use these as reference: {{examples}}

**Adjustments:** Apply the following refinements: {{adjustments}}

**Type:** Deliver your response as: {{output_type}}

**Extras:** {{extras}}

Combine your character's expertise with the request details. Use examples as a guide, apply all adjustments, produce the correct output type, and fulfill any extra requirements.
