from backend.dao.base_dao import BaseDao
from backend.dao.database import execute_query
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


class CategoryDao(BaseDao):
    def __init__(self):
        super().__init__(Category)
