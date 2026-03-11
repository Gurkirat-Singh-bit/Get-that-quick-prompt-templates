---
id: "security-audit"
title: "Security Audit: Vulnerability Scan for Code"
description: "A focused security audit prompt — scan code for OWASP Top 10 vulnerabilities, injection risks, auth gaps, and insecure patterns."
category: "fields/development"
tags: ["security", "audit", "owasp", "vulnerabilities", "penetration", "development"]
variables:
  - name: "code"
    label: "Code to Audit (paste function, module, API route, or full file)"
    required: true
  - name: "language"
    label: "Language / Framework"
    required: true
  - name: "threat_model"
    label: "Threat Model (who might attack this? e.g. external users, authenticated users, internal)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are a senior application security engineer. Perform a thorough security audit of the following {{language}} code.

**Threat Model:** {{threat_model}}

**Code:**
```
{{code}}
```

Audit against the following:

**OWASP Top 10 Checklist:**
- [ ] Injection (SQL, NoSQL, command, LDAP)
- [ ] Broken Authentication / weak session management
- [ ] Sensitive Data Exposure (secrets in code, weak encryption)
- [ ] XML External Entities (XXE)
- [ ] Broken Access Control (missing authorization checks)
- [ ] Security Misconfiguration (defaults, verbose errors)
- [ ] Cross-Site Scripting (XSS)
- [ ] Insecure Deserialization
- [ ] Using Components with Known Vulnerabilities
- [ ] Insufficient Logging & Monitoring

**Additional Checks:**
- Missing input validation or sanitization
- Race conditions or TOCTOU vulnerabilities
- Hardcoded credentials or secrets
- Overly permissive CORS or CSP headers
- Improper error handling that leaks internal details

For each vulnerability found:
- **Severity:** Critical / High / Medium / Low
- **Location:** Line or function
- **Description:** What the vulnerability is
- **Exploit scenario:** How an attacker could abuse it
- **Fix:** Concrete code-level remediation

End with a risk summary and the top 3 fixes to ship immediately.
