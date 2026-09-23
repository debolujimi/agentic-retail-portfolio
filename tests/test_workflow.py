import pytest

from demo.governance import GovernanceGate
from demo.models import AgentDecision, RetailSnapshot
from demo.workflow import RetailWorkflow


def make_snapshot(**overrides):
    data = {
        "store_id": "STORE-DEMO-001",
        "product": "Milk 1L",
        "current_stock": 18,
        "recent_weekly_sales": [22, 25, 24, 26],
        "supplier_lead_time_days": 2,
        "unit_price": 18.99,
    }
    data.update(overrides)
    return RetailSnapshot(**data)


def test_workflow_runs_all_five_agents():
    result = RetailWorkflow().run(make_snapshot())
    assert [d.agent for d in result.decisions] == [
        "demand_sensing",
        "inventory_management",
        "procurement",
        "pricing",
        "customer_engagement",
    ]


def test_governance_requires_human_review():
    result = RetailWorkflow().run(make_snapshot())
    assert result.governance_status == "review_required"
    assert result.requires_human_review is True
    assert result.approved is None


def test_high_demand_triggers_replenishment():
    result = RetailWorkflow().run(
        make_snapshot(current_stock=5, recent_weekly_sales=[30, 32, 31, 33])
    )
    procurement = next(d for d in result.decisions if d.agent == "procurement")
    assert procurement.data["recommended_order_quantity"] > 0


def test_low_stock_produces_high_stockout_risk():
    result = RetailWorkflow().run(
        make_snapshot(current_stock=5, recent_weekly_sales=[30, 32, 31, 33])
    )
    inventory = next(d for d in result.decisions if d.agent == "inventory_management")
    assert inventory.data["stockout_risk"] == "high"


def test_pricing_is_bounded():
    result = RetailWorkflow().run(make_snapshot(current_stock=100))
    pricing = next(d for d in result.decisions if d.agent == "pricing")
    assert abs(pricing.data["change_pct"]) <= 5.0


def test_workflow_is_deterministic_for_same_snapshot():
    workflow = RetailWorkflow()
    first = workflow.run(make_snapshot())
    second = workflow.run(make_snapshot())
    assert first == second


def test_large_procurement_recommendation_requires_review():
    result = RetailWorkflow().run(
        make_snapshot(current_stock=1, recent_weekly_sales=[40, 42, 41, 43])
    )
    procurement = next(d for d in result.decisions if d.agent == "procurement")
    assert procurement.data["recommended_order_quantity"] > 50
    assert result.governance_status == "review_required"
    assert result.requires_human_review is True


def test_governance_blocks_out_of_policy_price_change():
    decisions = [
        AgentDecision(
            agent="pricing",
            action="raise_price",
            rationale="Synthetic policy-boundary test.",
            data={"change_pct": 12.0},
        )
    ]
    status, requires_review = GovernanceGate().evaluate(decisions)
    assert status == "blocked"
    assert requires_review is True


@pytest.mark.parametrize(
    "overrides",
    [
        {"store_id": ""},
        {"product": ""},
        {"current_stock": -1},
        {"recent_weekly_sales": []},
        {"recent_weekly_sales": [10, -1, 12]},
        {"supplier_lead_time_days": -1},
        {"unit_price": 0},
    ],
)
def test_invalid_snapshot_inputs_fail_closed(overrides):
    with pytest.raises(ValueError):
        make_snapshot(**overrides)


def test_customer_agent_does_not_send_messages():
    result = RetailWorkflow().run(make_snapshot(current_stock=100))
    customer = next(d for d in result.decisions if d.agent == "customer_engagement")
    assert customer.data["channel"] == "demo_only"
