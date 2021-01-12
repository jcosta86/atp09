from backend.dao.database import select_query, insert_query


def read() -> list:
    list_categories = []
    query = 'SELECT name, description FROM category'
    select = select_query(query)
    for category in select:
        list_categories.append([category[0],category[1]])
    return list_categories


def write(name: str, description: str) -> None:
    query = f"INSERT into category(name, description) VALUES ('{name}','{description}')"
    insert_query(query)
