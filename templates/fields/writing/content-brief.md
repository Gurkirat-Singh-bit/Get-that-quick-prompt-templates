---
id: "content-brief"
title: "Content Brief: Full-Stack Article or Post Plan"
description: "Generate a complete content brief — angle, audience, structure, SEO, and key points — before writing a single word."
category: "fields/writing"
tags: ["content", "brief", "writing", "seo", "blog", "article", "marketing"]
variables:
  - name: "topic"
    label: "Topic (what is this content about?)"
    required: true
  - name: "target_audience"
    label: "Target Audience (who is this for? their knowledge level and goals)"
    required: true
  - name: "content_goal"
    label: "Content Goal (e.g. drive organic traffic, generate leads, build authority, educate)"
    required: true
  - name: "content_type"
    label: "Content Type (e.g. blog post, LinkedIn article, newsletter, video script)"
    required: true
  - name: "competitor_examples"
    label: "Competitor Examples (URLs or titles of similar content that ranks or performs well)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for creating a complete content brief.

The prompt is configured for the following inputs:
- Topic: {{topic}}
- Target audience: {{target_audience}}
- Content goal: {{content_goal}}
- Content type: {{content_type}}
- Competitor examples: {{competitor_examples}}

The generated prompt must instruct the AI agent to:

1. Act as a senior content strategist producing a brief that a writer can execute without additional context
2. Develop a unique angle with 3 hook options (and a recommendation on which to lead with), based on what differentiates this piece from the competitor examples
3. Profile the reader — who they are, what they already know, what question brought them here, and what they want to leave knowing or feeling
4. Identify the primary keyword and 3–5 secondary keywords, classify the search intent (informational / navigational / transactional / commercial), and suggest a title tag (under 60 characters) and meta description (under 160 characters)
5. Produce a full H2/H3 content outline — for each section, note the purpose, the key point to make, and the evidence or example needed
6. List 3–5 key insights the piece must include to be genuinely useful rather than surface-level
7. Flag clichés, worn-out angles, and common mistakes to avoid in this topic area
8. Recommend a CTA and the top 2–3 distribution channels for this piece

Output: the complete task delegation prompt only. Ready for Claude or a content strategy agent.
