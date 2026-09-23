from __future__ import annotations

from demo.models import AgentDecision


class CustomerEngagementAgent:
    name = "customer_engagement"

    def run(self, stockout_risk: str, pricing_action: str) -> AgentDecision:
        if stockout_risk == "high":
            action = "prepare_availability_notice"
        elif pricing_action == "consider_small_promotion":
            action = "prepare_promotion_message"
        else:
            action = "no_message"

        return AgentDecision(
            agent=self.name,
            action=action,
            rationale="Generates a non-sending customer communication recommendation for human review.",
            data={"channel": "demo_only"},
        )
