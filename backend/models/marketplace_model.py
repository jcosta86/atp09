from sqlalchemy import String, Column
from backend.models.base_model import BaseModel


class Marketplace(BaseModel): 
    __tablename__ = 'marketplace'

    __name = Column('name', String(length=200), nullable=False )
    __description = Column('description', String(length=200), nullable=True )

    def __init__(self, name: str, description: str, id: int = None) -> None:
        self.id = id
        self.name = name
        self.description = description

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError
        else:
            self.__name = value

    @description.setter
    def description(self, value: str) -> None:
        self.__description = value