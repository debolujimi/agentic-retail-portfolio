# Agentic Retail Portfolio

Governed multi-agent AI architecture for integrated retail decision support, human oversight and operational coordination.

[![Portfolio CI](https://github.com/debolujimi/agentic-retail-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/debolujimi/agentic-retail-portfolio/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Data](https://img.shields.io/badge/data-synthetic-success)

## Overview

This repository presents a portfolio implementation of a governed multi-agent retail decision-support architecture. It demonstrates how specialised AI agents can coordinate across interconnected retail functions while preserving human oversight, traceability, modularity and testability.

The implementation uses synthetic retail data and representative decision logic so that the engineering architecture can be reviewed independently of the underlying doctoral research system.

## System Architecture

The portfolio models five specialised operational agents:

1. **Demand Sensing Agent** — estimates near-term demand from synthetic sales history.
2. **Inventory Management Agent** — assesses stock coverage and replenishment risk.
3. **Procurement Agent** — recommends replenishment quantities.
4. **Pricing Agent** — proposes bounded pricing actions.
5. **Customer Engagement Agent** — proposes customer-facing actions from operational context.

A governance layer evaluates the combined recommendation before it can progress to a human review step.

```text
Synthetic Retail Data
        |
        v
Demand Sensing Agent
        |
        v
Inventory Management Agent
        |
        v
Procurement Agent
        |
        v
Pricing Agent
        |
        v
Customer Engagement Agent
        |
        v
Governance Gate
        |
        v
Human Review
        |
        v
Approved / Rejected Decision
```

## Engineering Focus

This portfolio demonstrates:

- multi-agent decomposition and orchestration;
- typed decision payloads and shared workflow state;
- human-in-the-loop approval;
- policy-based governance;
- auditable decision traces;
- synthetic test data;
- automated testing with `pytest`;
- continuous integration with GitHub Actions;
- modular Python architecture.

## Quick Start

```bash
git clone https://github.com/debolujimi/agentic-retail-portfolio.git
cd agentic-retail-portfolio

python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the demonstration:

```bash
python -m demo.app
```

Run the tests:

```bash
python -m pytest -q
```

## Repository Structure

```text
agentic-retail-portfolio/
├── .github/workflows/ci.yml
├── demo/
│   ├── agents/
│   ├── governance/
│   ├── synthetic_data/
│   ├── app.py
│   ├── models.py
│   └── workflow.py
├── docs/
│   ├── architecture.md
│   ├── engineering-decisions.md
│   ├── governance.md
│   └── testing-strategy.md
├── tests/
│   └── test_workflow.py
├── PORTFOLIO_SCOPE.md
├── SECURITY.md
├── requirements.txt
└── README.md
```

## Example Scenario

The demo uses a fictional retailer and synthetic inventory/sales values. No real retailer, participant or field-study records are included.

A typical run produces a structured recommendation, governance status, human-review requirement and an auditable sequence of agent decisions.

## Portfolio Scope

This repository is intended to demonstrate architecture and engineering practice. See [PORTFOLIO_SCOPE.md](PORTFOLIO_SCOPE.md) for the boundary between this portfolio and the underlying research implementation.

## Author

**Peter Olujimi**  
AI Engineer | Agentic AI Researcher | Applied AI & ML
