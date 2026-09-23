# Engineering Decisions

## Why Multiple Agents?
Retail decisions are interconnected but operationally distinct. Separating responsibilities into specialised agents improves modularity, observability, testing and failure isolation.

## Why Structured Decision Objects?
Each agent returns its identity, proposed action, rationale and structured data. This makes the workflow inspectable and supports logging, auditing and review interfaces.

## Why Human-in-the-Loop?
Inventory, procurement, pricing and customer communication can have financial or operational consequences. Outputs are therefore recommendations subject to governance and human review.

## Why Synthetic Data?
Synthetic data demonstrates the architecture without introducing participant, retailer or field-study information.

## Why Deterministic Demo Logic?
The repository is designed for inspectability. Deterministic representative logic makes tests reproducible while allowing production systems to place trained models, forecasting services or other AI components behind equivalent interfaces.
