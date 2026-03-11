---
id: "create-framework"
title: "CREATE Framework: Character, Request, Examples, Adjustments, Type, Extras"
description: "Generate a CREATE-structured agent prompt — the most detailed framework for complex, multi-constraint creative and professional delegation."
category: "frameworks/advanced"
tags: ["create", "framework", "prompt-generation", "complex", "detailed", "agent"]
variables:
  - name: "character"
    label: "Character (AI agent persona and expertise)"
    required: true
  - name: "request"
    label: "Request (what needs to be produced)"
    required: true
  - name: "examples"
    label: "Examples (reference work, samples, or style to model)"
    required: false
  - name: "adjustments"
    label: "Adjustments (constraints, modifications, or specific requirements)"
    required: true
  - name: "output_type"
    label: "Type (output type: code, essay, analysis, plan, email, etc.)"
    required: true
  - name: "extras"
    label: "Extras (any additional instructions or edge case handling)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a fully-loaded delegation prompt using the CREATE framework. This handles complex tasks where multiple constraints must be satisfied simultaneously.

Build it as follows:
- **C — Character:** Configure the agent as "{{character}}" — specific enough that it activates the right domain knowledge and voice.
- **R — Request:** State "{{request}}" precisely — the full ask, no assumed context.
- **E — Examples:** Use "{{examples}}" as the quality benchmark — instruct the agent to match this standard and explain where it diverges.
- **A — Adjustments:** Hard-enforce "{{adjustments}}" — these are non-negotiable constraints the agent must apply throughout.
- **T — Type:** Require output as "{{output_type}}" — specify format, structure, and length.
- **E — Extras:** Include "{{extras}}" as final instructions — edge cases, what to do if assumptions are needed, follow-up format.

Output: the complete CREATE prompt only. Dense but clear — every constraint woven into the agent's instructions so it needs no clarification. Ready for any AI agent workflow.
