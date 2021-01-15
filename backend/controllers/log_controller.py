from backend.dao.log_dao import LogDao
from backend.models.log_model import Log

DAO = LogDao()


def write_log(activity, domain_activity):
    log = Log(activity, domain_activity)
    DAO.write(log)


def read_log() -> list:
    log = DAO.read()
    return log
