from backend.dao.base_dao import BaseDao
from backend.models.category_model import Category


class CategoryDao(BaseDao):
    def __init__(self):
        super().__init__(Category)

    def create_table(self) -> None:
        query = f'''CREATE TABLE IF NOT EXISTS {self.table_name}(
                    id serial not null,
                    name varchar(45) not null,
                    description varchar(255) not null,
                    constraint {self.table_name}_pk primary key (id)
                );
                '''
        self.execute_query(query)
