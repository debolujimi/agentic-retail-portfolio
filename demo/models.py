from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class RetailSnapshot:
    store_id: str
    product: str
    current_stock: int
    recent_weekly_sales: list[int]
    supplier_lead_time_days: int
    unit_price: float


@dataclass
class AgentDecision:
    agent: str
    action: str
    rationale: str
    data: dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkflowResult:
    store_id: str
    product: str
    decisions: list[AgentDecision]
    governance_status: str
    requires_human_review: bool
    approved: bool | None = None
