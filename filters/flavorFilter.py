# filters/flavorFilter.py
from typing import List
from .interfaceWineFilter import IWineFilter
from model.wineReview import WineReview
from utils.translator import OfflineTranslator

class FlavorFilter(IWineFilter):
    """Filters wines based on friendly flavor profiles with synonym expansion and fallback."""
    
    SYNONYMS_MAP = {
        "smooth": ["smooth", "soft", "gentle", "easy", "silky"],
        "bold": ["bold", "full-bodied", "powerful", "heavy", "structured"],
        "fruity": ["fruity", "fruit", "cherry", "berry", "plum", "apple", "peach", "tropical"],
        "sweet": ["sweet", "honey", "jammy", "sugar", "off-dry"],
        "dry": ["dry", "crisp", "firm", "tannic"],
        "woody": ["woody", "oak", "barrel", "vanilla", "cedar"],
        "spicy": ["spicy", "pepper", "cinnamon", "clove"]
    }

    def apply(self, wines: List[WineReview], preference_value: str) -> List[WineReview]:
        if not preference_value or preference_value.lower() == 'cualquiera':
            return wines
        
        translated = OfflineTranslator.translate_flavor(preference_value)
        if translated == 'cualquiera':
            return wines
            
        search_terms = self.SYNONYMS_MAP.get(translated, [translated])
        
        matched_wines = []
        for w in wines:
            text_corpus = f"{w.description} {w.variety}".lower()
            if any(term in text_corpus for term in search_terms):
                matched_wines.append(w)
                
        if not matched_wines:
            print("   (Nota del Sommelier: No se encontró una coincidencia exacta de sabor, mostrando alternativas cercanas...)")
            return wines
            
        return matched_wines