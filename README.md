# GetThatQuick Prompt Templates

A curated collection of **220+ prompt templates** for [GetThatQuick](https://github.com/Gurkirat-Singh-bit/Get-that-quick-prompt-templates), a self-hosted prompt workbench.

## Categories

| Category | Description |
|---|---|
| `development` | Code refactoring, debugging, boilerplate generation |
| `development/devops` | CI/CD, Docker, automation |
| `development/database` | SQL, Prisma, schema design, migrations |
| `development/cloud` | AWS, Kubernetes, cloud infrastructure |
| `development/fullstack` | MERN, Django+React, full-stack apps |
| `development/frontend` | React, PWA, performance, web dev |
| `development/api` | REST APIs, OpenAPI, API gateways |
| `development/security` | JWT, authentication, security best practices |
| `development/architecture` | Event-driven, Kafka, CQRS |
| `development/infrastructure` | IaC, Terraform, CloudFormation |
| `development/debugging` | Monitoring, log analysis, memory leaks |
| `development/ai-ml` | ML models, RAG, agentic AI |
| `development/testing` | Unit tests, integration tests, QA |
| `creative/design` | UX/UI, wireframes, accessibility |
| `writing/marketing` | SEO, content strategy, email campaigns |

## Template Format

Each template is a Markdown file with YAML frontmatter:

```yaml
---
id: "template-slug"
title: "Template Title"
description: "One-line description"
category: "development"
tags: ["tag1", "tag2"]
variables:
  - name: "variable_name"
    label: "Variable Label"
    required: true
createdAt: "2026-03-01T00:00:00Z"
updatedAt: "2026-03-01T00:00:00Z"
---

System prompt body with {{variable_name}} placeholders...
```

## Source

Templates converted from [engineering-prompts](https://github.com/Hack-With-Hywepe/engineering-prompts) open-source community prompts.

## License

MIT
