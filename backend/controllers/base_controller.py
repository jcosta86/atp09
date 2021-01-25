from backend.dao.base_dao import BaseDao
from backend.models.base_model import BaseModel
# from backend.dao.log_dao import LogDao
# from backend.models.log_model import Log


class BaseController:
    def __init__(self, dao: BaseDao, domain_name: str):
        self.__dao = dao
        self.__domain_name = domain_name
        # self.__log = LogDao()

    def write(self, model: BaseModel) -> None:
        self.__dao.save(model)
        # self.__log.write(Log("Inserted", f"{self.__domain_name}"))

    def read_by_id(self, id: int) -> BaseModel:
        model = self.__dao.read_by_id(id)
        return model

    def read(self) -> list:
        list_all = self.__dao.read_all()
        # self.__log.write(Log("List", f"{self.__domain_name}"))
        return list_all

    def update(self, model: BaseModel) -> None:
        # self.__log.write(Log("Updated", f"{self.__domain_name} - {model.id}"))
        self.__dao.save(model)

    def delete(self, model: BaseModel) -> None:
        # self.__log.write(Log("Deleted", f"{self.__domain_name} - {id}"))
        self.__dao.delete(model)
