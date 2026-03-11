---
id: "tree-of-thought"
title: "Tree of Thought: Multi-Path Exploration Agent"
description: "Generate a Tree of Thought prompt to delegate open-ended problems to an AI agent — explores multiple solution paths before converging on the best."
category: "frameworks/reasoning"
tags: ["tree-of-thought", "tot", "exploration", "agent", "delegation", "branching"]
variables:
  - name: "problem"
    label: "Problem to Explore"
    required: true
  - name: "num_branches"
    label: "Number of Approaches to Explore (e.g. 3)"
    required: true
  - name: "domain"
    label: "Domain (what expertise the agent should bring)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a Tree of Thought delegation prompt. This prompt will force an AI agent to explore {{num_branches}} distinct solution paths before converging on a recommendation.

Configure it for:
- Problem: {{problem}}
- Domain: {{domain}}
- Branches to explore: {{num_branches}}

The generated prompt must instruct the agent to:
1. Establish itself as a {{domain}} expert
2. Explore exactly {{num_branches}} separate approaches — each treated as equally valid at the start
3. For each branch: state the approach, reason through it step by step, identify its strengths and weaknesses
4. After all branches, evaluate them comparatively on the most important criteria
5. Recommend the strongest path with explicit justification — or describe a hybrid if one is stronger

Output: the complete Tree of Thought prompt only. The agent receiving this must not collapse to a single answer prematurely. Ready for Claude, GPT, or any agent that can handle multi-turn reasoning.
