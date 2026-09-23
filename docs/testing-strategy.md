# Testing Strategy

## Objective
The portfolio tests architecture-level behaviour rather than reproducing the complete validation programme of the research implementation.

## Representative Tests
The test suite verifies that:
- all five agents execute in the expected order;
- governance requires human review;
- low-stock/high-demand conditions produce replenishment recommendations;
- inventory risk classification behaves as expected;
- pricing recommendations remain bounded.

## Reproducibility
Tests are deterministic and use synthetic fixtures.

## CI
GitHub Actions installs the minimal dependencies and runs:
```bash
python -m pytest -q
```
