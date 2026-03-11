---
id: "security-audit"
title: "Security Audit Agent: Task Delegation Prompt"
description: "Generate a task prompt to delegate a focused security audit to Claude or another AI agent — OWASP Top 10 scan with exploitability and fix guidance."
category: "fields/development"
tags: ["security", "audit", "owasp", "agent", "delegation", "vulnerability"]
variables:
  - name: "language"
    label: "Language / Framework"
    required: true
  - name: "scope"
    label: "Audit Scope (e.g. auth module, API routes, full codebase, specific file)"
    required: true
  - name: "threat_model"
    label: "Threat Model (who might attack this: external users, authenticated users, insiders)"
    required: true
  - name: "severity_threshold"
    label: "Report Threshold (e.g. report all findings / only High and Critical)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a security audit task prompt to hand to an AI agent (Claude, GPT, or a security-focused agent).

Configure it for:
- Language/stack: {{language}}
- Scope: {{scope}}
- Threat model: {{threat_model}}
- Report findings: {{severity_threshold}}

The generated prompt must instruct the agent to:
1. Adopt the role of a senior application security engineer performing a structured audit
2. Audit the provided code against OWASP Top 10: injection, broken auth, sensitive data exposure, XXE, broken access control, security misconfiguration, XSS, insecure deserialization, vulnerable components, insufficient logging
3. Also check: input validation, hardcoded secrets, race conditions, overly permissive CORS, error messages that leak internals
4. For each finding: severity (Critical/High/Medium/Low), exact location, description, exploit scenario (how an attacker would abuse it), concrete code-level fix
5. End with: risk summary, top 3 immediate fixes, and what would require a longer-term architectural change

Output: the complete security audit task prompt only. Ready to paste into a new Claude conversation or Cursor, then drop in the code to audit.
