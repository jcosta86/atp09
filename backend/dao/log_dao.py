from backend.dao.database import select_query, execute_query


def create_table_logfile():
    query = ''' CREATE TABLE IF NOT EXISTS logfile (
                id serial NOT NULL,
                date_activity date NULL DEFAULT 'now'::text::date,
                time_activity time NULL DEFAULT 'now'::text::time with time zone,
                activity varchar(20) NOT NULL,
                domain_activity varchar(20) NOT NULL,
                CONSTRAINT logfile_pk PRIMARY KEY (id)
            );
            '''
    execute_query(query)


def insert_log(activity: str, domain_activity: str) -> None:
    create_table_logfile()
    query = f"INSERT INTO logfile (activity, domain_activity) VALUES ('{activity}', '{domain_activity}')"
    execute_query(query)


def select_log():
    create_table_logfile()
    list_logs: list = []
    query = f"SELECT date_activity, time_activity, activity, domain_activity FROM logfile"
    logs_tuple = select_query(query)

    for obj in logs_tuple:
        list_logs.append([obj[0].strftime('%d/%m/%Y') + ' ' + obj[1].strftime('%H:%M:%S'), obj[2], obj[3]])
    return list_logs
