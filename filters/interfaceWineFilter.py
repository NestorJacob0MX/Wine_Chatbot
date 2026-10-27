from dataclasses import dataclass
from abc import ABC, abstractmethod
from model.wineReview import WineReview
from typing import List

class IWineFilter(ABC):
    @abstractmethod
    def apply(self, wines: List[WineReview], preference_value: str) -> List[WineReview]:
        pass