from backend.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'
    id = None
    name = str()
    description = str()

    def __init__(self, name: str, description: str, id: int = None) -> None:
        self.id = id
        self.name = name
        self.description = description
