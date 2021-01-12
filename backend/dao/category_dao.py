from backend.dao.database import select_query, execute_query


def create_table_category():
    query = '''CREATE TABLE IF NOT EXISTS category(
                id serial not null,
                name varchar(45) not null,
                description varchar(255) not null,
                constraint category_pk primary key (id)
            );
            '''
    execute_query(query)


def read() -> list:
    list_categories = []
    create_table_category()
    query = 'SELECT name, description FROM category'
    select = select_query(query)
    for category in select:
        list_categories.append([category[0],category[1]])
    return list_categories


def write(name: str, description: str) -> None:
    create_table_category()
    query = f"INSERT into category(name, description) VALUES ('{name}','{description}')"
    execute_query(query)
