---
id: "vibe-coding-spec"
title: "Vibe Coding Spec: AI-First Project Blueprint"
description: "Karpathy-inspired vibe coding spec — define your project in plain English and let AI build it iteratively. Structure your idea so the AI can execute with minimal ambiguity."
category: "fields/development"
tags: ["vibe-coding", "karpathy", "project-spec", "ai-coding", "rapid-prototype", "beginner"]
variables:
  - name: "project_name"
    label: "Project Name"
    required: true
  - name: "what_it_does"
    label: "What It Does (1-3 sentences, plain English)"
    required: true
  - name: "target_user"
    label: "Target User (who uses this and what problem does it solve?)"
    required: true
  - name: "core_features"
    label: "Core Features (list the 3-5 must-have features)"
    required: true
  - name: "tech_preferences"
    label: "Tech Preferences (preferred language, framework, or 'no preference')"
    required: true
  - name: "out_of_scope"
    label: "Out of Scope (what should NOT be built in this iteration)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

You are an expert full-stack developer. I want to build **{{project_name}}**.

**What it does:** {{what_it_does}}

**Target user:** {{target_user}}

**Core features to build:**
{{core_features}}

**Tech preferences:** {{tech_preferences}}

**Out of scope for now:** {{out_of_scope}}

Follow this build order:
1. Define the data model first — show me the schema before writing any UI or logic.
2. Start with mock/static data — do not connect a real database until the UI works.
3. Build one feature at a time — complete and test it before moving to the next.
4. Split code into multiple focused files — no mega-files.
5. After each feature, tell me what you built and what comes next.

Ask me any clarifying questions before starting. If requirements are unclear, make a decision and tell me what you chose.
