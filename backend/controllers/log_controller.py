from backend.dao.log_dao import LogDao
from backend.models.log_model import Log

DAO = LogDao()

class LogController:
    def read_log(self) -> list:
        log = DAO.read()
        return log
