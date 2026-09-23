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

    def __post_init__(self) -> None:
        if not self.store_id.strip():
            raise ValueError("store_id must not be empty")
        if not self.product.strip():
            raise ValueError("product must not be empty")
        if self.current_stock < 0:
            raise ValueError("current_stock must be non-negative")
        if not self.recent_weekly_sales:
            raise ValueError("recent_weekly_sales must contain at least one observation")
        if any(value < 0 for value in self.recent_weekly_sales):
            raise ValueError("sales observations must be non-negative")
        if self.supplier_lead_time_days < 0:
            raise ValueError("supplier_lead_time_days must be non-negative")
        if self.unit_price <= 0:
            raise ValueError("unit_price must be greater than zero")


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
