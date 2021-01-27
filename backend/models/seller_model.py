from sqlalchemy import Column, String

from backend.models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'
    
    __fullname = Column('fullname', String(length=200), nullable = False)
    __email = Column('email', String(length=200), nullable = False)
    __phone = Column('phone', String(length=200), nullable = False)

    def __init__(self, fullname: str, email: str, phone: str, id: int = None):
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.id = id

    @property
    def fullname(self) -> str:
        return self.__fullname

    @property
    def email(self) -> str:
        return self.__email

    @property
    def phone(self) -> str:
        return self.__phone

    @fullname.setter
    def fullname(self, value: str) -> None:
        if not value:
            raise ValueError
        else:
            self.__fullname = value

    @email.setter
    def email(self, value: str) -> None:
        if not value:
            raise ValueError
        else:
            self.__email = value

    @phone.setter
    def phone(self, value: str) -> None:
        if not value:
            raise ValueError
        else:
            self.__phone = value
