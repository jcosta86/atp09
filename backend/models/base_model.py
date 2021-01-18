class BaseModel:
    __tablename__: str = str()

    def __init__(self, id: int = None):
        self.__id = id

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id