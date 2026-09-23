from __future__ import annotations

from demo.models import AgentDecision


class GovernanceGate:
    """Representative governance rules for the portfolio demo."""

    def evaluate(self, decisions: list[AgentDecision]) -> tuple[str, bool]:
        pricing = next((d for d in decisions if d.agent == "pricing"), None)
        procurement = next((d for d in decisions if d.agent == "procurement"), None)

        if pricing and abs(float(pricing.data.get("change_pct", 0.0))) > 5.0:
            return "blocked", True

        if procurement and int(procurement.data.get("recommended_order_quantity", 0)) > 50:
            return "review_required", True

        return "review_required", True
