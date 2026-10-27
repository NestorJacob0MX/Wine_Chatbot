# utils/translator.py
import difflib

class OfflineTranslator:
    """Provides offline bilingual translation and synonym matching for Spanish to English queries."""
    
    FLAVOR_MAP = {
        "suave": "smooth",
        "ligero": "light",
        "fuerte": "bold",
        "robusto": "robust",
        "afrutado": "fruity",
        "frutal": "fruity",
        "dulce": "sweet",
        "seco": "dry",
        "amaderado": "woody",
        "roble": "oak",
        "especiado": "spicy"
    }

    PAIRING_MAP = {
        "carne": "beef",
        "carnes rojas": "red meat",
        "pollo": "chicken",
        "pescado": "fish",
        "mariscos": "seafood",
        "pastas": "pasta",
        "quesos": "cheese",
        "tapas": "tapas",
        "postres": "dessert"
    }

    @staticmethod
    def translate_flavor(spanish_input: str) -> str:
        clean_input = spanish_input.strip().lower()
        if not clean_input or clean_input == 'cualquiera':
            return 'cualquiera'
            
        keys = list(OfflineTranslator.FLAVOR_MAP.keys())
        match = difflib.get_close_matches(clean_input, keys, n=1, cutoff=0.4)
        
        if match:
            translated = OfflineTranslator.FLAVOR_MAP[match[0]]
            print(f"   (Traducción offline: '{spanish_input}' -> '{translated}')")
            return translated
        return clean_input

    @staticmethod
    def translate_pairing(spanish_input: str) -> str:
        clean_input = spanish_input.strip().lower()
        if not clean_input or clean_input == 'cualquiera':
            return 'cualquiera'
            
        keys = list(OfflineTranslator.PAIRING_MAP.keys())
        match = difflib.get_close_matches(clean_input, keys, n=1, cutoff=0.4)
        
        if match:
            translated = OfflineTranslator.PAIRING_MAP[match[0]]
            print(f"   (Traducción offline: '{spanish_input}' -> '{translated}')")
            return translated
        return clean_input