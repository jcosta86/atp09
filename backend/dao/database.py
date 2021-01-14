from backend.dao.connection import Connection


def execute_query(query: str) -> None:
    with Connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()


def select_query(query: str) -> list:
    with Connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            connection.commit()

    return result
