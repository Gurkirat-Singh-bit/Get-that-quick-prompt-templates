---
id: "chain-of-thought"
title: "Chain of Thought: Step-by-Step Reasoning Agent"
description: "Generate a Chain of Thought prompt to delegate analytical or complex problems to an AI agent — forces visible, sequential reasoning before any conclusion."
category: "frameworks/reasoning"
tags: ["chain-of-thought", "cot", "reasoning", "agent", "delegation", "analytical"]
variables:
  - name: "problem"
    label: "Problem or Question (what needs deep reasoning?)"
    required: true
  - name: "domain"
    label: "Domain (e.g. software architecture, financial analysis, medical diagnosis)"
    required: true
  - name: "constraints"
    label: "Constraints (what the reasoning must stay within)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a Chain of Thought delegation prompt for the following problem. This prompt will be given to an AI agent (Claude, GPT, Cursor) that must reason through the problem visibly before giving any answer.

Configure it for:
- Problem: {{problem}}
- Domain expertise required: {{domain}}
- Constraints: {{constraints}}

The generated prompt must:
1. Establish the agent's role as a rigorous {{domain}} expert
2. Present the problem clearly with all necessary context
3. Include an explicit instruction: "Do not give your final answer first. Think step by step. Number each reasoning step. Only state your conclusion after the reasoning chain is complete."
4. Require the agent to flag every assumption it makes
5. End with a format requirement for the final answer

Output: the complete Chain of Thought prompt only. Ready to paste into Claude, ChatGPT, Cursor, or any reasoning-capable agent. The agent receiving this must show all work.
