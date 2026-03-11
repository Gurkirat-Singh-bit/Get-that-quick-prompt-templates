---
id: "refactor-recipe"
title: "Refactor Recipe: Structured Code Improvement"
description: "Refactor code with a clear goal — improve readability, reduce complexity, apply design patterns, or optimize performance without changing behavior."
category: "fields/development"
tags: ["refactor", "clean-code", "solid", "readability", "development", "engineering"]
variables:
  - name: "code"
    label: "Code to Refactor"
    required: true
  - name: "language"
    label: "Language / Framework"
    required: true
  - name: "refactor_goal"
    label: "Refactor Goal (e.g. readability, extract functions, apply SOLID, reduce duplication, performance)"
    required: true
  - name: "must_not_change"
    label: "Must Not Change (behavior, interfaces, or constraints to preserve)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are a senior {{language}} engineer. Refactor the following code.

**Refactor Goal:** {{refactor_goal}}

**Must Not Change:** {{must_not_change}}

**Original Code:**
```
{{code}}
```

Follow this process:
1. **Analyze** — Describe the current problems with the code (complexity, duplication, naming, violations of principles).
2. **Plan** — List the specific refactoring steps you will take before touching the code.
3. **Refactor** — Provide the fully refactored version.
4. **Explain** — For each significant change, explain *why* it is better.
5. **Verify** — Confirm that the external behavior and interfaces are unchanged. Note any assumptions made.

Do not over-engineer. Make only the changes needed to achieve the stated goal. Leave a comment in the code where a further refactor opportunity exists but was intentionally left out of scope.
