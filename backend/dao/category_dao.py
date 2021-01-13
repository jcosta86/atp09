from backend.dao.database import select_query, execute_query
from backend.models.category_model import Category

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
    query = 'SELECT name, description, id FROM category'
    select = select_query(query)
    for item in select:
        category = Category(item[0], item[1], item[2])
        list_categories.append(category)
    return list_categories


def write(category: Category) -> None:
    create_table_category()
    query = f"INSERT into category(name, description) VALUES ('{category.name}','{category.description}')"
    execute_query(query)


def update(category: Category) -> None:
    query = f"UPDATE category SET name = '{category.name}', description = '{category.description}' WHERE id = '{category.id}'"
    execute_query(query)


def delete(id: int) -> None:
    query = f"DELETE FROM category WHERE id = '{id}'"
    execute_query(query)