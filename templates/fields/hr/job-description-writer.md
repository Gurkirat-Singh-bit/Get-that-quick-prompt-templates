---
id: "job-description-writer"
title: "Job Description Writer: Bias-Reduced, Compelling JD"
description: "Write a clear, inclusive job description that attracts the right candidates — avoiding jargon, reducing bias, and focusing on outcomes over credentials."
category: "fields/hr"
tags: ["hr", "hiring", "job-description", "recruiting", "bias-reduction", "talent"]
variables:
  - name: "role_title"
    label: "Role Title"
    required: true
  - name: "team_context"
    label: "Team Context (what team, what they work on, stage of company)"
    required: true
  - name: "core_responsibilities"
    label: "Core Responsibilities (what will this person actually do day-to-day?)"
    required: true
  - name: "success_criteria"
    label: "Success Criteria (what does great look like in 6 months?)"
    required: true
  - name: "must_haves"
    label: "Must-Haves (non-negotiable skills or experience)"
    required: true
  - name: "nice_to_haves"
    label: "Nice-to-Haves (preferred but not required)"
    required: false
  - name: "comp_range"
    label: "Compensation Range (salary, equity, benefits headline)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for writing a bias-reduced, compelling job description.

The prompt is configured for the following variables: role title, team context, core responsibilities, success criteria, must-haves, nice-to-haves, and compensation range.

The generated prompt must instruct the AI agent to:

1. Act as a senior recruiter and people ops leader who understands how job descriptions attract or repel candidates
2. Write a JD that follows these non-negotiable rules:
   - Lead with company mission and team impact, not a list of requirements
   - Frame all responsibilities as outcomes using "You will own X" not "Responsibilities include X"
   - Replace years-of-experience requirements with skill and capability descriptions
   - Avoid gendered language — use "they", avoid "rockstar", "ninja", "aggressive", "dominant"
   - Cap the must-haves list at 5 items maximum
   - Include the compensation range
3. Use this exact structure: company overview (2 sentences, mission-focused), role overview (what this person owns and why it matters), what you'll do (5–7 outcome-oriented bullets), what we're looking for (must-haves only, skills not years), nice to have (brief), what we offer (comp, benefits, culture), how to apply
4. After the JD, produce a separate bias audit: flag any phrases that may introduce unconscious bias and suggest a replacement for each flagged phrase

Output: the complete task delegation prompt only. Ready for Claude or an HR agent.
