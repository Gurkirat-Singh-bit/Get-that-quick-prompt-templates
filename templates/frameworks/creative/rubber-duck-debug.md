---
id: "rubber-duck-debug"
title: "Rubber Duck: Explain-to-Understand Agent Prompt"
description: "Generate a prompt to delegate deep explanation to an AI agent — forces first-principles teaching that exposes any gaps in understanding."
category: "frameworks/creative"
tags: ["rubber-duck", "teaching", "explanation", "first-principles", "agent", "delegation"]
variables:
  - name: "subject"
    label: "Subject (concept, system, or code to explain)"
    required: true
  - name: "audience_level"
    label: "Audience Level (e.g. complete beginner, non-technical executive, junior dev)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a Rubber Duck explanation agent prompt. The AI agent receiving this must explain {{subject}} to {{audience_level}} with zero assumed knowledge.

The generated prompt must instruct the agent to:
1. Explain what it is in the simplest possible language — ban jargon. If technical terms are unavoidable, define them in plain language immediately.
2. Explain why it exists — what problem does it solve?
3. Explain how it works — use an analogy from everyday life and walk through a concrete example
4. Expose what's commonly misunderstood or oversimplified about it
5. Rebuild the explanation from first principles — derive it without appealing to authority
6. Close with a single sentence that captures the complete idea accurately

If the agent notices its explanation has gaps or contradictions, it must call them out explicitly.

Output: the complete rubber duck explanation agent prompt only. The agent receiving this should produce an explanation that would genuinely enlighten a {{audience_level}}. Ready for Claude, GPT, or any explanatory AI agent.
