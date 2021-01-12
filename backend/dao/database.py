import psycopg2
import os

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')


def execute_query(query: str) -> None:  # Function for use with insert and create query
    connection_string = f"host={host} user={user} dbname={database} password={password}"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


def select_query(query: str) -> list:  # Function for return values (Use with select)
    connection_string = f"host={host} user={user} dbname={database} password={password}"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

    return result
