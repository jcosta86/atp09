from backend.models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'

    def __init__(self, fullname: str, email: str, phone: str, id: int = None):
        super().__init__(id)
        self.__fullname = fullname
        self.__email = email
        self.__phone = phone

    @property
    def fullname(self) -> str:
        return self.__fullname

    @fullname.setter
    def fullname(self, value: str):
        self.__fullname = value

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str):
        self.__email = value

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        self.__phone = value
