from backend.models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import MONEY


class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(length=45), nullable = False)
    description = Column(String(length=255), nullable = False)
    price = Column(MONEY(), nullable = False)

    def __init__(self, name: str, description: str, price: float, id: int = None) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.id = id
