from backend.models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'
    id = None
    fullname = str()
    email = str()
    phone = str()

    def __init__(self, fullname: str, email: str, phone: str, id: int = None):
        self.id = id
        self.fullname = fullname
        self.email = email
        self.phone = phone
