from backend.dao.database import select_query, insert_query
from datetime import datetime


def insert_log(activity: str, domain_activity: str) -> None:
    query = f"INSERT INTO logfile (activity, domain_activity) VALUES ('{activity}', '{domain_activity}')"
    insert_query(query)


def select_log():
    list_logs: list = []
    query = f"SELECT date_activity, time_activity, activity, domain_activity FROM logfile"
    logs_tuple = select_query(query)
    print(logs_tuple)

    for obj in logs_tuple:
        print(obj[0].strftime('%d/%m/%Y'))
        print(obj[1].strftime('%H:%M:%S'))
        list_logs.append([obj[0].strftime('%d/%m/%Y')+' '+obj[1].strftime('%H:%M:%S'), obj[2], obj[3]])
    return list_logs
