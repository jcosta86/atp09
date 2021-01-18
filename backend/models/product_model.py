from backend.models.base_model import BaseModel


class Product(BaseModel):
    __tablename__ = 'product'

    def __init__(self, name: str, description: str, price: float, id: int = None) -> None:
        super().__init__(id)
        self.__name = name
        self.__description = description
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def price(self) -> float:
        return self.__price

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @description.setter
    def description(self, value: str) -> None:
        self.__description = value
    
    @price.setter
    def price(self, value: float) -> None:
        self.__price = value
