import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Session:
    def __init__(self) -> None:
        connector = os.getenv('DB_CONNECTOR')
        host = os.getenv('DB_HOST')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        dbname = os.getenv('DB_NAME')
        self.__connection_string = f"{connector}://{user}:{password}@{host}:5432/{dbname}"

    def __enter__(self):
        self.__engine = create_engine(self.__connection_string)
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()
        self.__engine.dispose()