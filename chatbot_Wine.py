import sys
from filters.countryFilter import CountryFilter
from filters.varietyFilter import VarietyFilter
from filters.priceFilter import PriceFilter
from filters.flavorFilter import FlavorFilter
from filters.pairingFilter import PairingFilter
from loader.loader import WineDatasetRepository
from engine.recommendationEngine import RecommendationEngine
from chatbot.wineChatbot import WineChatbot

if __name__ == "__main__":
    repo = WineDatasetRepository()
    filters = {
        #"country": CountryFilter(),
        #"variety": VarietyFilter(),
        "flavor": FlavorFilter(),
        "pairing": PairingFilter(),
        "price": PriceFilter()
    }
    engine = RecommendationEngine(filters)
    chatbot = WineChatbot(repo, engine)

    try:
        chatbot.start_conversation()
    except KeyboardInterrupt:
        print("\n\n¡Hasta luego! Vuelve cuando busques una nueva botella.")
        sys.exit(0)