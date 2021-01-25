from sqlalchemy import String, Column
from backend.models.base_model import BaseModel


class Marketplace(BaseModel): 
    __tablename__ = 'marketplace'

    name = Column( String(length=200), nullable=False )
    description = Column( String(length=200), nullable=True )

    def __init__(self, name:str, description:str) -> None:
        self.name = name
        self.description = description
