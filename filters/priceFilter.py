from dataclasses import dataclass
from model.wineReview import WineReview
from filters.interfaceWineFilter import IWineFilter
from typing import List

class PriceFilter(IWineFilter):
    """Filters wines based on maximum price constraint."""
    def apply(self, wines: List[WineReview], preference_value: str) -> List[WineReview]:
        if not preference_value or preference_value.lower() == 'cualquiera':
            return wines
        try:
            max_price = float(preference_value)
            return [w for w in wines if w.price is not None and w.price <= max_price]
        except ValueError:
            return wines