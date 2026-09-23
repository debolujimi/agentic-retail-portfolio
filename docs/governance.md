# Governance and Human Oversight

## Principle
The system separates recommendation generation from approval authority.

## Governance Flow
1. Agents generate recommendations.
2. Recommendations enter shared workflow state.
3. Policy rules inspect potentially consequential actions.
4. The workflow is marked for human review.
5. Approval or rejection occurs outside autonomous agent execution.

## Representative Rules
The demonstration includes illustrative rules such as:
- pricing adjustments above a defined threshold are blocked;
- unusually large replenishment recommendations require review;
- operational recommendations remain reviewable.

These rules are illustrative and are not commercial policy.

## Auditability
Every agent returns a structured decision with rationale and data, allowing the sequence to be persisted or rendered in a review interface without relying on opaque internal state.
