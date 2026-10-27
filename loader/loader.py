# data_loader.py
import pandas as pd
from typing import List
from model.wineReview import WineReview

class WineDatasetRepository:
    """Loads and manages the Kaggle Wine Reviews dataset, adhering to Single Responsibility."""
    
    def __init__(self, file_path: str = "./dataset/wines.csv") -> None:
        self._file_path = file_path
        self._wines: List[WineReview] = []
        self._load_data()

    def _load_data(self) -> None:
        try:
            df = pd.read_csv(self._file_path)
            df = df.dropna(subset=['title', 'country', 'variety', 'points', 'description'])
            
            for _, row in df.iterrows():
                self._wines.append(
                    WineReview(
                        title=str(row.get('title', 'N/A')),
                        country=str(row.get('country', 'N/A')),
                        variety=str(row.get('variety', 'N/A')),
                        province=str(row.get('province', 'N/A')),
                        price=float(row['price']) if pd.notna(row.get('price')) else 0.0,
                        points=int(row.get('points', 80)),
                        description=str(row.get('description', '')),
                        winery=str(row.get('winery', 'N/A'))
                    )
                )
            print(f"Dataset cargado exitosamente")
        except FileNotFoundError:
            print(f"Archivo '{self._file_path}' no encontrado.")

    def get_all_wines(self) -> List[WineReview]:
        """Returns the complete collection of typed wine review entities."""
        return self._wines