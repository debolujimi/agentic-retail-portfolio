from __future__ import annotations

from demo.models import AgentDecision, RetailSnapshot


class DemandSensingAgent:
    name = "demand_sensing"

    def run(self, snapshot: RetailSnapshot) -> AgentDecision:
        if not snapshot.recent_weekly_sales:
            forecast = 0.0
        else:
            forecast = sum(snapshot.recent_weekly_sales) / len(snapshot.recent_weekly_sales)

        return AgentDecision(
            agent=self.name,
            action="estimate_demand",
            rationale="Uses a simple moving average over synthetic weekly sales.",
            data={"forecast_weekly_units": round(forecast, 2)},
        )
