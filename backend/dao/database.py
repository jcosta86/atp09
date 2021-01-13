import psycopg2
import os

HOST = os.getenv('DB_HOST')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
DATABASE = os.getenv('DB_NAME')

CONNECTION_STRING = f"host={HOST} user={USER} dbname={DATABASE} password={PASSWORD}"


def execute_query(query: str) -> None:
    with psycopg2.connect(CONNECTION_STRING) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()


def select_query(query: str) -> list:
    with psycopg2.connect(CONNECTION_STRING) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()

    return result
