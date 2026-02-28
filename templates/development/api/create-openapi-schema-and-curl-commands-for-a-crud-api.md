---
id: "create-openapi-schema-and-curl-commands-for-a-crud-api"
title: "Create OpenAPI Schema and Curl Commands for a CRUD API"
description: "Create an OpenAPI schema for a simple CRUD API with the following endpoints: `GET /items`, `POST /items`, `PUT /items/{{."
category: "development/api"
tags: ["openapi", "schema", "curl", "commands", "crud"]
variables:
  - name: "id"
    label: "Id"
    required: true
createdAt: "2026-03-01T00:00:00Z"
updatedAt: "2026-03-01T00:00:00Z"
---

Create an OpenAPI schema for a simple CRUD API with the following endpoints: `GET /items`, `POST /items`, `PUT /items/{{id}}`, and `DELETE /items/{{id}}`. Based on the schema, generate `curl` commands to test these endpoints with sample data, including headers and request bodies as necessary.
