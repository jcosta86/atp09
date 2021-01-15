from backend.dao.base_dao import BaseDao
from backend.models.base_model import BaseModel
from backend.dao.log_dao import LogDao
from backend.models.log_model import Log


class BaseController:
    def __init__(self,dao: BaseDao, domain_name: str):
        self.dao = dao
        self.domain_name = domain_name
        self.log = LogDao()

    def write(self, model: BaseModel) -> None:
        self.dao.write(model)
        self.log.write(Log("Inserted", f"{self.domain_name}"))

    def read_by_id(self, id: int) -> BaseModel:
        model = self.dao.read_by_id(id)
        return model

    def read(self) -> list:
        list_all = self.dao.read()
        self.log.write(Log("List", f"{self.domain_name}"))
        return list_all

    def update(self,model: BaseModel) -> None:
        self.log.write(Log("Updated", f"{self.domain_name} - {model.id}"))
        self.dao.update(model)

    def delete(self,id: int) -> None:
        self.log.write(Log("Deleted", f"{self.domain_name} - {id}"))
        self.dao.delete(id)
