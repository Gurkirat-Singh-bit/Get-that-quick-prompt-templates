# GetThatQuick Prompt Templates

A curated collection of **55 prompt templates** for [GetThatQuick](https://github.com/Gurkirat-Singh-bit/Get-that-quick), a self-hosted prompt workbench.

Two collections:
- **Framework Templates** — 27 templates implementing proven prompt engineering frameworks (RTF, RISEN, CO-STAR, Chain of Thought, etc.)
- **Field Templates** — 28 battle-tested workflows for real professional use cases (development, product, design, business, writing, learning)

## Categories

| Category | Templates | Description |
|---|---|---|
| `frameworks/basic` | 5 | Simple 3-part frameworks — RTF, TAG, APE, STAR, 5Ws |
| `frameworks/structured` | 5 | Intermediate 4-5 part frameworks — RISEN, RACE, CARE, COAST, CREO |
| `frameworks/advanced` | 6 | Complex multi-part frameworks — CRISPE, CO-STAR, ROSES, CREATE, TRACE, MASTER |
| `frameworks/reasoning` | 5 | Reasoning techniques — Chain of Thought, Tree of Thought, ReAct, Few-Shot, Zero-Shot CoT |
| `frameworks/goal-oriented` | 4 | Planning frameworks — SMART Goals, PAIN, 4Ds, SOAR |
| `frameworks/creative` | 3 | Creative & persuasion frameworks — Perspective Shift, Rubber Duck, Before-After-Bridge |

## Framework Index

### Basic
| ID | Framework | Best For |
|---|---|---|
| `rtf-framework` | **RTF** — Role, Task, Format | Quick structured prompts |
| `tag-framework` | **TAG** — Task, Action, Goal | Simple task execution |
| `ape-framework` | **APE** — Action, Purpose, Expectation | Targeted outputs |
| `star-framework` | **STAR** — Situation, Task, Action, Result | Narrative & case studies |
| `5ws-framework` | **5Ws** — Who, What, When, Where, Why | Research & analysis |

### Structured
| ID | Framework | Best For |
|---|---|---|
| `risen-framework` | **RISEN** — Role, Instructions, Steps, End Goal, Narrowing | Complex repeatable tasks |
| `race-framework` | **RACE** — Role, Action, Context, Expectation | Role-based instructions |
| `care-framework` | **CARE** — Context, Action, Result, Example | High-precision outputs |
| `coast-framework` | **COAST** — Context, Objective, Actions, Scenario, Task | Strategic planning |
| `creo-framework` | **CREO** — Context, Role, Evidence, Output | Evidence-backed responses |

### Advanced
| ID | Framework | Best For |
|---|---|---|
| `crispe-framework` | **CRISPE** — Capacity, Insight, Statement, Personality, Experiment | Expert-level customization |
| `co-star-framework` | **CO-STAR** — Context, Objective, Style, Tone, Audience, Response | Content & communications |
| `roses-framework` | **ROSES** — Role, Objective, Scenario, Expected Solution, Steps | Structured problem-solving |
| `create-framework` | **CREATE** — Character, Request, Examples, Adjustments, Type, Extras | Complex multi-step projects |
| `trace-framework` | **TRACE** — Topic, Reason, Audience, Counterargument, Evidence | Persuasive arguments |
| `master-framework` | **MASTER** — Mindset, Audience, Style, Tone, Expertise, Rules | Fully customized interactions |

### Reasoning
| ID | Framework | Best For |
|---|---|---|
| `chain-of-thought` | **Chain of Thought** — Sequential reasoning | Math, logic, analysis |
| `tree-of-thought` | **Tree of Thought** — Multi-path exploration | Open-ended problems |
| `react-framework` | **ReAct** — Reasoning + Acting cycles | Agentic, iterative tasks |
| `few-shot-framework` | **Few-Shot** — Example-guided generation | Pattern replication |
| `zero-shot-cot` | **Zero-Shot CoT** — "Let's think step by step" | Quick reasoning boost |

### Goal-Oriented
| ID | Framework | Best For |
|---|---|---|
| `smart-goals-framework` | **SMART Goals** — Specific, Measurable, Achievable, Relevant, Time-bound | Goal planning |
| `pain-framework` | **PAIN** — Problem, Amplify, Insight, Next Steps | Problem-solving & persuasion |
| `4ds-framework` | **4Ds** — Define, Delimit, Direct, Detail | Project scoping |
| `soar-framework` | **SOAR** — Strengths, Opportunities, Aspirations, Results | Strategic analysis |

### Creative
| ID | Framework | Best For |
|---|---|---|
| `perspective-shift` | **Perspective Shift** — Multi-viewpoint analysis | Decision-making, bias detection |
| `rubber-duck-debug` | **Rubber Duck** — Explain to understand | Teaching, simplification |
| `before-after-bridge` | **Before-After-Bridge** — Transformation narrative | Copywriting, pitches |

## Template Format

Each template is a Markdown file with YAML frontmatter:

```yaml
---
id: "template-slug"
title: "Template Title"
description: "One-line description"
category: "frameworks/basic"
tags: ["tag1", "tag2"]
variables:
  - name: "variable_name"
    label: "Variable Label"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Prompt body using {{variable_name}} placeholders...
```

---

## Field Templates (`templates/fields/`)

Battle-tested workflows for real professional use cases, inspired by Andrej Karpathy, Satya Nadella, and proven PM/UX/writing playbooks.

### Development
| ID | Template | What It Does |
|---|---|---|
| `context-engineering` | **Context Engineering** | Karpathy-style — load the right context before asking AI to code |
| `vibe-coding-spec` | **Vibe Coding Spec** | Define a project so AI can build it iteratively without ambiguity |
| `code-review-deep` | **Deep Code Review** | Security, performance, correctness, maintainability |
| `security-audit` | **Security Audit** | Full OWASP Top 10 vulnerability scan |
| `refactor-recipe` | **Refactor Recipe** | Structured refactor with clear goals and invariants |
| `tech-debt-analysis` | **Tech Debt Analysis** | Inventory, prioritize, and plan a 90-day debt remediation |

### Product Management
| ID | Template | What It Does |
|---|---|---|
| `prd-writer` | **PRD Writer** | Full Product Requirements Document |
| `user-story-mapper` | **User Story Mapper** | INVEST stories with acceptance criteria |
| `launch-readiness` | **Launch Readiness** | Go/no-go assessment with probability rating (Nadella-inspired) |
| `metric-diagnosis` | **Metric Diagnosis** | Root-cause investigation of any metric drop or spike |
| `feature-prioritization` | **Feature Prioritization** | RICE + MoSCoW scoring for backlog decisions |

### Design & UX
| ID | Template | What It Does |
|---|---|---|
| `user-persona` | **User Persona** | Rich persona with JTBD, pain points, and design implications |
| `ux-audit` | **UX Audit** | Nielsen heuristics-based usability review |
| `user-interview-script` | **Interview Script** | Research-ready interview guide with probing questions |

### Business & Strategy
| ID | Template | What It Does |
|---|---|---|
| `meeting-prep` | **Meeting Prep** | Context-aware briefing before any meeting (Nadella-inspired) |
| `time-audit` | **Time Audit** | Reveal gaps between priorities and actual calendar |
| `decision-memo` | **Decision Memo** | Structured options analysis with clear recommendation |
| `competitive-analysis` | **Competitive Analysis** | Landscape map, competitor profiles, white space |

### Writing & Content
| ID | Template | What It Does |
|---|---|---|
| `content-brief` | **Content Brief** | Full strategy brief before writing any piece |
| `repurpose-content` | **Content Repurposing** | Transform one piece into 5+ platform-optimized formats |
| `cold-email-sequence` | **Cold Email Sequence** | 3-touch outreach sequence that earns replies |

### Learning
| ID | Template | What It Does |
|---|---|---|
| `feynman-explainer` | **Feynman Explainer** | Explain any concept from first principles |
| `study-plan` | **Study Plan** | Personalized curriculum with milestones and resources |
| `socratic-debate` | **Socratic Debate** | Stress-test any claim or belief through questioning |

---

## Template Format

Each template is a Markdown file with YAML frontmatter:

```yaml
---
id: "template-slug"
title: "Template Title"
description: "One-line description"
category: "frameworks/basic"
tags: ["tag1", "tag2"]
variables:
  - name: "variable_name"
    label: "Variable Label"
    required: true
createdAt: "2026-03-11T00:00:00Z"
updatedAt: "2026-03-11T00:00:00Z"
---

Prompt body using {{variable_name}} placeholders...
```

## License

MIT
