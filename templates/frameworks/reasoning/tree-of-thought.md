---
id: "tree-of-thought"
title: "Tree of Thought: Multi-Path Exploration"
description: "Explore multiple distinct reasoning paths simultaneously before converging on the best solution — ideal for complex, open-ended problems."
category: "frameworks/reasoning"
tags: ["tree-of-thought", "tot", "branching", "reasoning", "exploration", "problem-solving", "evaluation"]
variables:
  - name: "problem"
    label: "Problem (the challenge to explore)"
    required: true
  - name: "num_branches"
    label: "Number of Approaches (how many paths to explore, e.g. 3)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

**Problem:** {{problem}}

Explore {{num_branches}} distinct approaches to solving this problem using a Tree of Thought.

For each approach:

**Branch [N]: [Approach Name]**
- Initial assumption or angle
- Step-by-step logic along this path
- Potential solution or outcome
- Strengths of this approach
- Weaknesses or risks of this approach

---

After exploring all {{num_branches}} branches, evaluate them comparatively. Recommend the most promising path and explain clearly why it outperforms the alternatives. If a hybrid of multiple approaches is stronger, describe it.
