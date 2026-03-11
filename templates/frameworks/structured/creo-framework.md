---
id: "creo-framework"
title: "CREO Framework: Context, Role, Evidence, Output"
description: "Generate evidence-backed, accurate responses by specifying Context, assigning a Role, providing Evidence, and defining the Output format."
category: "frameworks/structured"
tags: ["creo", "framework", "context", "role", "evidence", "output", "intermediate", "factual"]
variables:
  - name: "context"
    label: "Context (situation or topic area)"
    required: true
  - name: "role"
    label: "Role (expert persona)"
    required: true
  - name: "evidence"
    label: "Evidence (data, facts, references, or constraints to use)"
    required: true
  - name: "output_format"
    label: "Output (desired format or structure)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

**Context:** {{context}}

**Role:** You are {{role}}.

**Evidence:** Ground your response in the following: {{evidence}}

**Output:** Deliver your response in this format: {{output_format}}

Leverage your expertise and the provided evidence to produce an accurate, well-supported response in the requested output format. Do not go beyond the scope of the evidence provided.
