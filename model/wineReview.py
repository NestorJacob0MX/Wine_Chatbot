from dataclasses import dataclass

@dataclass
class WineReview:
    """Represents a wine review entity from the Kaggle dataset."""
    title: str
    country: str
    variety: str
    province: str
    price: float
    points: int
    description: str
    winery: str