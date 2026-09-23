from __future__ import annotations

from demo.agents import (
    CustomerEngagementAgent,
    DemandSensingAgent,
    InventoryManagementAgent,
    PricingAgent,
    ProcurementAgent,
)
from demo.governance import GovernanceGate
from demo.models import RetailSnapshot, WorkflowResult


class RetailWorkflow:
    def __init__(self) -> None:
        self.demand = DemandSensingAgent()
        self.inventory = InventoryManagementAgent()
        self.procurement = ProcurementAgent()
        self.pricing = PricingAgent()
        self.customer = CustomerEngagementAgent()
        self.governance = GovernanceGate()

    def run(self, snapshot: RetailSnapshot) -> WorkflowResult:
        decisions = []

        demand = self.demand.run(snapshot)
        decisions.append(demand)
        forecast = float(demand.data["forecast_weekly_units"])

        inventory = self.inventory.run(snapshot, forecast)
        decisions.append(inventory)
        risk = str(inventory.data["stockout_risk"])

        procurement = self.procurement.run(snapshot, forecast)
        decisions.append(procurement)

        pricing = self.pricing.run(snapshot, risk)
        decisions.append(pricing)

        customer = self.customer.run(risk, pricing.action)
        decisions.append(customer)

        governance_status, requires_review = self.governance.evaluate(decisions)

        return WorkflowResult(
            store_id=snapshot.store_id,
            product=snapshot.product,
            decisions=decisions,
            governance_status=governance_status,
            requires_human_review=requires_review,
        )
