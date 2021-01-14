from backend.dao.base_dao import BaseDao
from backend.dao.database import select_query, execute_query
from backend.models.log_model import Log


def create_table_logfile():
    query = ''' CREATE TABLE IF NOT EXISTS logfile (
                id serial NOT NULL,
                date_activity date NOT NULL,
                time_activity time NOT NULL,
                activity varchar(500) NOT NULL,
                domain_activity varchar(500) NOT NULL,
                CONSTRAINT logfile_pk PRIMARY KEY (id)
            );
            '''
    execute_query(query)


class LogDao(BaseDao):
    def __init__(self):
        super().__init__(Log)


def insert_log(log: Log) -> None:
    query = f"INSERT INTO logfile (activity, domain_activity) VALUES ('{log.activity}', '{log.domain_activity}');"
    execute_query(query)


def select_log():
    list_logs: list = []
    query = f"SELECT date_activity, time_activity, activity, domain_activity FROM logfile;"
    logs_tuple = select_query(query)

    for obj in logs_tuple:
        log = Log(date_activity=obj[0].strftime('%d/%m/%Y'),
                  time_activity=obj[1].strftime('%H:%M:%S'),
                  activity=obj[2],
                  domain_activity=obj[3])
        list_logs.append(log)
    return list_logs


dao = LogDao()
print(dao.read()[0].date_activity)
