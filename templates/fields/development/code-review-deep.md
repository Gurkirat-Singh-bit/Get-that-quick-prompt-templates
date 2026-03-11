---
id: "code-review-deep"
title: "Deep Code Review: Security, Performance, Maintainability"
description: "A thorough code review covering correctness, security vulnerabilities, performance bottlenecks, maintainability, and edge cases."
category: "fields/development"
tags: ["code-review", "security", "performance", "maintainability", "bugs", "development"]
variables:
  - name: "code"
    label: "Code to Review (paste the full function, module, or PR diff)"
    required: true
  - name: "language"
    label: "Language / Framework"
    required: true
  - name: "context"
    label: "Context (what does this code do? where does it fit in the system?)"
    required: true
  - name: "focus"
    label: "Review Focus (e.g. security, performance, all, specific concern)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are a senior {{language}} engineer conducting a thorough code review. Review the following code with an expert eye.

**Context:** {{context}}

**Code:**
```
{{code}}
```

**Review Focus:** {{focus}}

Review across all of the following dimensions:

**1. Correctness**
- Logic errors, off-by-one issues, incorrect assumptions
- Unhandled edge cases and null/undefined states
- Incorrect data transformations

**2. Security**
- Injection vulnerabilities (SQL, XSS, command injection)
- Insecure data handling, exposure of sensitive data
- Authentication/authorization gaps
- Missing input validation

**3. Performance**
- Unnecessary re-renders, N+1 queries, or redundant computations
- Missing indexes, inefficient data structures
- Blocking operations that should be async

**4. Maintainability**
- Naming clarity, overly complex logic
- Missing or misleading comments
- Violations of SOLID or DRY principles
- Hard-coded values that should be configurable

**5. Error Handling**
- Silent failures, overly broad catch blocks
- Missing or low-quality error messages
- Unhandled promise rejections

For each issue found: state the **severity** (critical / major / minor), the **line/area**, and a **concrete fix**.
End with an overall assessment and a prioritized list of the top 3 changes to make first.
