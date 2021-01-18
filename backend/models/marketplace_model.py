from backend.models.base_model import BaseModel


class Marketplace(BaseModel):
    __tablename__ = 'marketplace'

    def __init__(self, name: str, description: str, id: int = None):
        super().__init__(id)
        self.__name = name
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value
