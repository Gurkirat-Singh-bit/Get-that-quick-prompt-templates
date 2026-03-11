---
id: "hard-conversation-prep"
title: "Hard Conversation Prep: Difficult Talk Planning"
description: "Prepare for any difficult conversation — with a colleague, partner, parent, or friend — so you say what you mean without damaging the relationship."
category: "fields/personal"
tags: ["communication", "difficult-conversations", "relationships", "conflict", "personal", "reddit"]
variables:
  - name: "situation"
    label: "The Situation (what happened, what needs to be addressed)"
    required: true
  - name: "person"
    label: "The Person (their role and your relationship to them)"
    required: true
  - name: "your_goal"
    label: "Your Goal (what do you want to achieve from this conversation?)"
    required: true
  - name: "your_fear"
    label: "Your Fear (what are you most worried about saying or hearing?)"
    required: false
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Generate a task delegation prompt for preparing for a difficult conversation.

The prompt is configured for the following inputs:
- Situation: {{situation}}
- Person: {{person}}
- Your goal: {{your_goal}}
- Your fear: {{your_fear}}

The generated prompt must instruct the AI agent to:

1. Act as an expert communication coach — the goal is to prepare the user to say what they need to say without damaging the relationship
2. Work through these eight preparation steps:
   - **Clarify the Real Intention**: distinguish between wanting to be heard, wanting them to change, wanting a decision, or wanting closure — clarity on intention prevents conversations from going sideways before they start
   - **Steelman Their Perspective**: explain what might be driving the other person's behavior or position from their own experience — what are they feeling or fearing that the user may not have fully considered?
   - **Write the Opening 3 Sentences**: the hardest part is starting — write an opening that states the topic directly (no burying it), signals the user wants to understand and not just to win, and does not immediately trigger defensiveness
   - **Distill the Core Message**: in 1–2 sentences, what is the single most important thing the user needs to say — not everything, just the one thing
   - **A Strategy for When It Gets Hard**: when something triggers the user during the conversation, what is the plan — offer a specific breathing technique or pause strategy to use in the moment
   - **Phrases to Avoid**: 3–4 specific phrases that will almost certainly derail this conversation, with a suggested alternative for each
   - **Define Success Before Starting**: what does a successful conversation look like — even if the other person does not change, leaving having said what needed to be said with the other person feeling heard is a win
   - **Exit Plan if It Escalates**: how to pause the conversation productively without abandoning it if it escalates beyond what is useful

Output: the complete task delegation prompt only. Ready for Claude.
