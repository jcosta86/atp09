from backend.models.base_model import BaseModel


class Product(BaseModel):
    __tablename__ = 'product'
    id = None
    name = str()
    description = str()
    price = float()

    def __init__(self, name: str, description: str, price: float, id: int = None) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.price = price
