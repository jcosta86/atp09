from backend.dao.log_dao import select_log, insert_log
from backend.models.log import Log


def create_log(activity, domain_activity):
    log = Log(activity, domain_activity)
    insert_log(log)


def read_log() -> list:
    log = select_log()
    return log
