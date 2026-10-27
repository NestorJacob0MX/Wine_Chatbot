from dataclasses import dataclass
from typing import List, Dict
from model.wineReview import WineReview
from filters.interfaceWineFilter import IWineFilter
from loader.loader import WineDatasetRepository
from helpers.topRecomendations import RecommendationCriterion

class RecommendationEngine:
    """Applies rule-based filters sequentially to the wine repository."""
    def __init__(self, filters: Dict[str, IWineFilter]) -> None:
        self._filters = filters

    def recommend(self, repository: WineDatasetRepository, user_preferences: Dict[str, str]) -> List[WineReview]:
        current_wines = repository.get_all_wines()
        
        for criterion, value in user_preferences.items():
            if criterion in self._filters and value:
                current_wines = self._filters[criterion].apply(current_wines, value)
                
        current_wines.sort(key=lambda x: x.points, reverse=True)
        return current_wines[:RecommendationCriterion.top_recomendations.value]