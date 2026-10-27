# filters/pairingFilter.py
from typing import List
from .interfaceWineFilter import IWineFilter
from model.wineReview import WineReview
from utils.translator import OfflineTranslator

class PairingFilter(IWineFilter):
    """Filters wines based on friendly food pairing preferences with synonym expansion and fallback."""
    
    PAIRING_SYNONYMS = {
        "beef": ["beef", "steak", "red meat", "meat", "lamb"],
        "red meat": ["beef", "steak", "red meat", "meat", "lamb"],
        "chicken": ["chicken", "poultry", "turkey"],
        "fish": ["fish", "seafood", "salmon", "shellfish", "white fish"],
        "pasta": ["pasta", "spaghetti", "lasagna", "italian"],
        "cheese": ["cheese", "cheddar", "brie", "gouda", "charcuterie"],
        "tapas": ["tapas", "appetizers", "snacks", "hors d'oeuvres"],
        "dessert": ["dessert", "chocolate", "cake", "sweet"]
    }

    def apply(self, wines: List[WineReview], preference_value: str) -> List[WineReview]:
        if not preference_value or preference_value.lower() == 'cualquiera':
            return wines
        
        translated = OfflineTranslator.translate_pairing(preference_value)
        if translated == 'cualquiera':
            return wines
            
        search_terms = self.PAIRING_SYNONYMS.get(translated, [translated])
        
        matched_wines = []
        for w in wines:
            text_corpus = f"{w.description} {w.variety} {w.title}".lower()
            if any(term in text_corpus for term in search_terms):
                matched_wines.append(w)
                
        if not matched_wines:
            print("   (Nota del Sommelier: No se encontró una coincidencia exacta de maridaje, mostrando alternativas cercanas...)")
            return wines
            
        return matched_wines