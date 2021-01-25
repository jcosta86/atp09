from backend.models.base_model import BaseModel
from sqlalchemy import Column, String


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(length=45))
    description = Column(String(length=255))

    def __init__(self, name: str, description: str, id: int = None) -> None:
        self.id = id
        self.name = name
        self.description = description


'''
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
'''
