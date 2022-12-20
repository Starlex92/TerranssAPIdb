from datetime import datetime

from beanie import Document
from pydantic import BaseModel
from typing import Optional

class ProductReview(Document):
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    class Settings:
        name = "product_review"
    
    class Config:
        schema_extra = {
            "example": {
                "name": "testss",
                "product": "voiture",
                "rating": 4.9,
                "review": "Excellente voiture",
                "date": datetime.now()
            }
        }

class UpdateProductReview(BaseModel):
    name: Optional[str]
    product: Optional[str]
    rating: Optional[float]
    review: Optional[str]
    date: Optional[datetime]
    
    class Config:
        schema_extra = {
            "example": {
                "name": "testss updated",
                "product": "voiture de course",
                "rating": 5.0,
                "review": "Excellente voiture tres rapide",
                "date": datetime.now()
            }
        }