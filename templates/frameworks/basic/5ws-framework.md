---
id: "5ws-framework"
title: "5Ws Framework: Who, What, When, Where, Why"
description: "Generate a 5Ws-structured prompt to delegate thorough research or analysis to an AI agent — covering all five dimensions."
category: "frameworks/basic"
tags: ["5ws", "framework", "prompt-generation", "research", "analysis", "agent"]
variables:
  - name: "topic"
    label: "Topic or Subject to Investigate"
    required: true
  - name: "depth"
    label: "Depth Required (quick overview / detailed analysis / exhaustive breakdown)"
    required: true
  - name: "output_format"
    label: "Output Format (e.g. report, structured breakdown, executive summary)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a ready-to-use research prompt using the 5Ws (Who, What, When, Where, Why) framework for the topic: "{{topic}}".

The prompt must instruct the agent to:
- Investigate at depth level: {{depth}}
- Cover all five dimensions without skipping any
- Structure output as: {{output_format}}
- Conclude with a synthesis that connects all five Ws into a coherent picture

The generated prompt should establish the agent's role as a thorough researcher, give it the topic, and specify exactly how to structure and deliver the 5Ws analysis.

Output: the complete 5Ws prompt only. No meta-commentary. Ready to hand to Claude, Perplexity, or any research-capable AI agent.
