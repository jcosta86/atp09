from backend.dao.log_dao import select_log


def read_log() -> list:
    log = select_log()
    return log