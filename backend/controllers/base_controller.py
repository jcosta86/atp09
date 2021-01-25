from backend.dao.base_dao import BaseDao
from backend.models.base_model import BaseModel
from backend.controllers.log_controller import LogController
from backend.models.log_model import Log


class BaseController:
    def __init__(self, dao: BaseDao, domain_name: str):
        self.__dao = dao
        self.__domain_name = domain_name
        self.__log_controller = LogController()

    def write(self, model: BaseModel) -> None:
        self.__dao.save(model)
        self.__log_controller.create(Log("Inserted", f"{self.__domain_name}"))

    def read_by_id(self, id: int) -> BaseModel:
        model = self.__dao.read_by_id(id)
        return model

    def read(self) -> list:
        list_all = self.__dao.read_all()
        self.__log_controller.create(Log("List", f"{self.__domain_name}"))
        return list_all

    def update(self, model: BaseModel) -> None:
        self.__log_controller.create(Log("Updated", f"{self.__domain_name} - {model.id}"))
        self.__dao.save(model)

    def delete(self, model: BaseModel) -> None:
        self.__log_controller.create(Log("Deleted", f"{self.__domain_name} - {model.id}"))
        self.__dao.delete(model)
