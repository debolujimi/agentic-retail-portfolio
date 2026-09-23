from __future__ import annotations

from demo.models import AgentDecision, RetailSnapshot


class InventoryManagementAgent:
    name = "inventory_management"

    def run(self, snapshot: RetailSnapshot, forecast_weekly_units: float) -> AgentDecision:
        weeks_of_cover = (
            snapshot.current_stock / forecast_weekly_units
            if forecast_weekly_units > 0
            else float("inf")
        )
        risk = "high" if weeks_of_cover < 1.0 else "medium" if weeks_of_cover < 2.0 else "low"

        return AgentDecision(
            agent=self.name,
            action="assess_stock_risk",
            rationale="Compares current stock with forecast demand to estimate stock-cover risk.",
            data={
                "weeks_of_cover": round(weeks_of_cover, 2) if weeks_of_cover != float("inf") else None,
                "stockout_risk": risk,
            },
        )
