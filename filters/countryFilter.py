from dataclasses import dataclass
from model.wineReview import WineReview
from filters.interfaceWineFilter import IWineFilter
from typing import List
import difflib
from helpers.fuzzymatchingPercent import FuzzyMatchingPercent

class CountryFilter(IWineFilter):
    """Filters wines by country with fuzzy matching support for typos."""
    def apply(self, wines: List[WineReview], preference_value: str) -> List[WineReview]:
        if not preference_value or preference_value.lower() == 'cualquiera':
            return wines
        
        available_countries = list(set(w.country for w in wines if w.country))
        match = difflib.get_close_matches(preference_value, available_countries, n=1, cutoff=FuzzyMatchingPercent.percent.value)
        
        if match:
            target = match[0]
            print(f"   (Coincidencia para país: '{target}')")
            return [w for w in wines if w.country and w.country.lower() == target.lower()]
        return []