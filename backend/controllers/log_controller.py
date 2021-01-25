from backend.dao.log_dao import LogDao

DAO = LogDao()

class LogController:
    # def read_log(self) -> list:
    #     log = DAO.read_all()
    #     return log

    def create(self, model) -> None:
        DAO.save(model)


    def read_all(self) -> list:
        return DAO.read_all()
