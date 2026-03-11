---
id: "react-framework"
title: "ReAct Framework: Reasoning + Acting"
description: "Combine reasoning and action in an interleaved loop — alternate between Thought, Action, and Observation cycles for dynamic, iterative problem-solving."
category: "frameworks/reasoning"
tags: ["react", "reasoning", "acting", "thought", "observation", "agentic", "problem-solving", "iterative"]
variables:
  - name: "task"
    label: "Task (what needs to be accomplished?)"
    required: true
  - name: "available_tools"
    label: "Available Tools or Resources (what can be used to complete this?)"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

**Task:** {{task}}

**Available Tools/Resources:** {{available_tools}}

Work through this task using the ReAct (Reasoning + Acting) pattern. Interleave thought and action until the task is complete:

- **Thought [N]:** What do I know so far? What is the next logical step?
- **Action [N]:** Execute a specific step using the available tools or resources.
- **Observation [N]:** What did I learn from this action? What changed? What should I do next?

Repeat this Thought → Action → Observation cycle until you reach a complete solution.

**Final Answer:** Provide a clear, complete response to the original task that synthesizes all observations.
