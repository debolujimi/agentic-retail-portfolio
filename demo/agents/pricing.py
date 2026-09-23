from __future__ import annotations

from demo.models import AgentDecision, RetailSnapshot


class PricingAgent:
    name = "pricing"

    def run(self, snapshot: RetailSnapshot, stockout_risk: str) -> AgentDecision:
        if stockout_risk == "high":
            change_pct = 0.0
            action = "hold_price"
        elif stockout_risk == "low" and snapshot.current_stock > 0:
            change_pct = -2.0
            action = "consider_small_promotion"
        else:
            change_pct = 0.0
            action = "hold_price"

        proposed_price = snapshot.unit_price * (1 + change_pct / 100)

        return AgentDecision(
            agent=self.name,
            action=action,
            rationale="Applies a bounded demonstration rule rather than autonomous dynamic pricing.",
            data={
                "current_price": round(snapshot.unit_price, 2),
                "proposed_price": round(proposed_price, 2),
                "change_pct": change_pct,
            },
        )
