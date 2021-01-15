from backend.models.base_model import BaseModel


class Marketplace(BaseModel):
    __tablename__ = 'marketplace'
    id = None
    name = str()
    description = str()

    def __init__(self, name: str, description: str, id: int = None):
        self.id = id
        self.name = name
        self.description = description
