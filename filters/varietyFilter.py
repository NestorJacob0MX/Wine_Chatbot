from dataclasses import dataclass
from model.wineReview import WineReview
from filters.interfaceWineFilter import IWineFilter
from typing import List
import difflib
from helpers.fuzzymatchingPercent import FuzzyMatchingPercent

class VarietyFilter(IWineFilter):
    """Filters wines by variety (e.g., Pinot Noir, Cabernet Sauvignon) with fuzzy matching."""
    def apply(self, wines: List[WineReview], preference_value: str) -> List[WineReview]:
        if not preference_value or preference_value.lower() == 'cualquiera':
            return wines
            
        available_varieties = list(set(w.variety for w in wines if w.variety))
        match = difflib.get_close_matches(preference_value, available_varieties, n=1, cutoff=FuzzyMatchingPercent.percent.value)
        
        if match:
            target = match[0]
            print(f"(Coincidencia para Variedad: '{target}')")
            return [w for w in wines if w.variety and w.variety.lower() == target.lower()]
        return []