from dataclasses import dataclass
from typing import List
from loader.loader import WineDatasetRepository
from engine.recommendationEngine import RecommendationEngine
from model.wineReview import WineReview

class WineChatbot:
    """Manages conversation flow and fuzzy correction feedback in Latin American Spanish."""
    def __init__(self, repository: WineDatasetRepository, engine: RecommendationEngine) -> None:
        self._repository = repository
        self._engine = engine

    def start_conversation(self) -> None:
        print("=" * 70)
        print(" 🍷 ¡Hola! Qué gusto saludarte. Bienvenido a tu Sommelier Inteligente.")
        print(" Estoy aquí para ayudarte a descubrir el vino ideal para ti, sin")
        print(" complicaciones ni tecnicismos. ¡Vamos a encontrar tu copa perfecta!")
        print("=" * 70 + "\n")

        preferences = {}

        print("✨ Para ti, ¿cómo se siente el vino ideal en el paladar?")
        print("   (Puedes elegir opciones sencillas como: suave, fuerte, afrutado, dulce, seco...)")
        preferences["flavor"] = input("Tu elección (o escribe 'cualquiera'): ").strip()
        print()

        print("🍽️ Excelente. ¿Con qué platillo o comida planeas acompañarlo hoy?")
        print("   (Por ejemplo: carnes rojas, pollo, pescado, pastas, quesos, tapas, o escribe 'cualquiera')")
        preferences["pairing"] = input("Tu elección: ").strip()
        print()

        print("💰 Por último, ¿cuál sería tu presupuesto máximo aproximado en dólares?")
        preferences["price"] = input("Tu elección (ej. 30 o escribe 'cualquiera'): ").strip()
        
        print("\n" + "=" * 70)
        print(" 🔎 ¡Perfecto! Estoy consultando nuestra cava para buscar las mejores opciones...")
        print("=" * 70 + "\n")

        recommendations = self._engine.recommend(self._repository, preferences)
        self._display_results(recommendations)

    def _display_results(self, recommendations: List[WineReview]) -> None:
        if not recommendations:
            print("Lo siento, no encontré vinos que coincidan exactamente con esos criterios o correcciones.")
            print("Te sugiero reiniciar la búsqueda con términos más amplios.")
        else:
            print(f" ✨ ¡He encontrado {len(recommendations)} recomendación(es) ideal(es) para ti:\n")
            for i, wine in enumerate(recommendations, 1):
                print(f"{i}. **{wine.title}**")
                print(f"   - País: {wine.country} ({wine.province}) | Variedad: {wine.variety}")
                print(f"   - Puntuación: {wine.points} pts 🏆 | Precio: ${wine.price if wine.price > 0 else 'No especificado'}")
                print(f"   - Nota del sommelier: \"{wine.description[:150]}...\"")
                print("=" * 70 + "\n")
        print("\n 🥂 ¡Salud! Gracias por usar nuestro asistente basado en reglas.")