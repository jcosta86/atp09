class BaseModel:
    __tablename__: str = str()

    def __init__(self, id: int):
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id
