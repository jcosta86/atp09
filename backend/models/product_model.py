from backend.models.base_model import BaseModel
from sqlalchemy import Column, String, Float

class Product(BaseModel):
    __tablename__ = 'product'

    __name = Column('name', String(length=45), nullable = False)
    __description = Column('description', String(length=255), nullable = False)
    __price = Column('price', Float(), nullable = False)

    def __init__(self, name: str, description: str, price: float, id: int = None) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.id = id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def price(self) -> str:
        return self.__price

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError
        else:
            self.__name = value

    @description.setter
    def description(self, value: str) -> None:
        self.__description = value

    @price.setter
    def price(self, value: float) -> None:
        self.__price = value
