from __future__ import annotations

from dataclasses import asdict
from pprint import pprint

from demo.models import RetailSnapshot
from demo.workflow import RetailWorkflow


def main() -> None:
    snapshot = RetailSnapshot(
        store_id="STORE-DEMO-001",
        product="Milk 1L",
        current_stock=18,
        recent_weekly_sales=[22, 25, 24, 26],
        supplier_lead_time_days=2,
        unit_price=18.99,
    )

    result = RetailWorkflow().run(snapshot)
    pprint(asdict(result), sort_dicts=False)


if __name__ == "__main__":
    main()
