from __future__ import annotations

import math

from demo.models import AgentDecision, RetailSnapshot


class ProcurementAgent:
    name = "procurement"

    def run(self, snapshot: RetailSnapshot, forecast_weekly_units: float) -> AgentDecision:
        target_weeks = 2
        target_stock = math.ceil(forecast_weekly_units * target_weeks)
        order_qty = max(0, target_stock - snapshot.current_stock)

        return AgentDecision(
            agent=self.name,
            action="recommend_replenishment",
            rationale="Targets approximately two weeks of forecast demand in the demonstration.",
            data={
                "recommended_order_quantity": order_qty,
                "supplier_lead_time_days": snapshot.supplier_lead_time_days,
            },
        )
