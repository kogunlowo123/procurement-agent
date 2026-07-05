# Procurement Agent

[![CI](https://github.com/kogunlowo123/procurement-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/procurement-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Finance | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Procurement automation agent that manages purchase requisitions, evaluates vendor proposals, automates RFP processes, tracks contract compliance, and optimizes procurement spend.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `create_requisition` | Create a purchase requisition with specifications and budget |
| `evaluate_proposals` | Evaluate and score vendor proposals against criteria |
| `generate_rfp` | Generate a Request for Proposal document |
| `track_contract` | Track contract compliance, renewals, and spend |
| `analyze_spend` | Analyze procurement spend by category, vendor, and department |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/procurement/process` | Process transaction |
| `POST` | `/api/v1/procurement/analyze` | Analyze data |
| `POST` | `/api/v1/procurement/validate` | Validate |
| `POST` | `/api/v1/procurement/report` | Generate report |
| `GET` | `/api/v1/procurement/audit` | Get audit trail |

## Features

- Procurement
- Compliance
- Reporting

## Integrations

- Netsuite
- Quickbooks
- Xero
- Sap
- Oracle Financials

## Architecture

```
procurement-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── procurement_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**ERP + Accounting Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
