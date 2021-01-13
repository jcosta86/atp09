from backend.dao.database import select_query, execute_query
from backend.models.log_model import Log


def create_table_logfile():
    query = ''' CREATE TABLE IF NOT EXISTS logfile (
                id serial NOT NULL,
                date_activity date NULL DEFAULT 'now'::text::date,
                time_activity time NULL DEFAULT 'now'::text::time with time zone,
                activity varchar(500) NOT NULL,
                domain_activity varchar(500) NOT NULL,
                CONSTRAINT logfile_pk PRIMARY KEY (id)
            );
            '''
    execute_query(query)


def insert_log(log: Log) -> None:
    create_table_logfile()
    query = f"INSERT INTO logfile (activity, domain_activity) VALUES ('{log.activity}', '{log.domain_activity}')"
    execute_query(query)


def select_log():
    create_table_logfile()
    list_logs: list = []
    query = f"SELECT date_activity, time_activity, activity, domain_activity FROM logfile"
    logs_tuple = select_query(query)

    for obj in logs_tuple:
        log = Log(date_activity=obj[0].strftime('%d/%m/%Y'),
                  time_activity=obj[1].strftime('%H:%M:%S'),
                  activity=obj[2],
                  domain_activity=obj[3])
        list_logs.append(log)
    return list_logs
