import os

import psycopg2


class Connection:
    def __get_connection_string(self):
        host = os.getenv('DB_HOST')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        dbname = os.getenv('DB_NAME')
        connection_string = f'host={host} user={user} password={password} dbname={dbname}'
        return connection_string

    def __enter__(self):
        self.__connection = psycopg2.connect(self.__get_connection_string())
        return self.__connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__connection.close()
