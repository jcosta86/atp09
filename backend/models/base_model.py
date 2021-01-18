class BaseModel:
    __tablename__ = str()

    def __init__(self, id: int = None):
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
