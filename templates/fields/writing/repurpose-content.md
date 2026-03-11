---
id: "repurpose-content"
title: "Content Repurposing: One Piece → Multiple Formats"
description: "Transform a single piece of content into 5+ formats optimized for different platforms and audiences."
category: "fields/writing"
tags: ["repurpose", "content", "social-media", "distribution", "writing", "marketing"]
variables:
  - name: "source_content"
    label: "Source Content (paste or describe the original piece)"
    required: true
  - name: "original_format"
    label: "Original Format (e.g. blog post, podcast transcript, webinar recording)"
    required: true
  - name: "target_formats"
    label: "Target Formats (e.g. LinkedIn post, Twitter thread, email newsletter, TikTok script, YouTube short)"
    required: true
  - name: "brand_voice"
    label: "Brand Voice (e.g. professional and direct, conversational and witty)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for repurposing a piece of content into multiple platform-native formats.

The prompt is configured for the following inputs:
- Source content: {{source_content}}
- Original format: {{original_format}}
- Target formats: {{target_formats}}
- Brand voice: {{brand_voice}}

The generated prompt must instruct the AI agent to:

1. Act as a senior content strategist and copywriter who deeply understands platform-specific content behavior
2. Produce a fully written, platform-ready version for each target format — not an outline, but the actual finished content
3. Follow platform-specific rules for each format encountered:
   - LinkedIn post: hook in line 1, value across 3–5 short paragraphs, CTA at the end, 150–300 words, no hashtag spam
   - Twitter/X thread: 5–8 tweets, tweet 1 is the hook and must work as a standalone, each tweet is a self-contained idea, final tweet ties it together
   - Email newsletter: subject line with an A/B variant, preview text, opening hook, 3 key points, one clear CTA
   - TikTok/Reel script: hook in the first 3 seconds, main point, pattern interrupt, CTA — under 60 seconds when spoken
   - YouTube short description: algorithm-optimized with keyword placement and CTA
4. Maintain the specified brand voice consistently across all formats
5. For each format, include a brief note on what was emphasized, compressed, or reframed — and why — for that platform's audience behavior

Output: the complete task delegation prompt only. Ready for Claude or any writing agent.
