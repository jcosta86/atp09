from sqlalchemy import Column, String

from backend.models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'
    
    fullname = Column(String(length=200), nullable = False)
    email = Column(String(length=200), nullable = False)
    phone = Column(String(length=200), nullable = False)

    def __init__(self, fullname: str, email: str, phone: str, id: int = None):
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.id = id
