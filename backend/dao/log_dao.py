from backend.dao.base_dao import BaseDao
from backend.models.log_model import Log


class LogDao(BaseDao):
    def __init__(self):
        super().__init__(Log)


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
    LogDao.execute_query(query)
