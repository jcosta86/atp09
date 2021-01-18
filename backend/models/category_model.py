from backend.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'

    def __init__(self, name: str, description: str, id: int = None) -> None:
        super().__init__(id)
        self.__id = id
        self.__name = name
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @description.setter
    def description(self, value: str) -> None:
        self.__description = value
