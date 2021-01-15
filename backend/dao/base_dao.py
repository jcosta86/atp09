from psycopg2.extras import DictCursor, DictRow

from backend.dao.connection import Connection
from backend.models.base_model import BaseModel


class BaseDao:
    def __init__(self, model: type(BaseModel)):
        self.model = model
        self.table_name = self.model.__tablename__

    @staticmethod
    def execute_query(query: str) -> None:
        with Connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()

    @staticmethod
    def select_all_query(query: str) -> list:
        with Connection() as connection:
            with connection.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                connection.commit()
        return result

    @staticmethod
    def select_one_query(query: str) -> DictRow:
        with Connection() as connection:
            with connection.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                connection.commit()
        return result

    def _get_db_columns_names(self) -> str:
        separator = ', '
        model_attributes = vars(self.model)
        columns_names = [key for key, value in model_attributes.items() if not key.startswith('__')]
        return separator.join(columns_names)

    def _get_db_columns_names_without_id(self) -> str:
        separator = ', '
        model_attributes = vars(self.model)
        columns_names = [key for key, value in model_attributes.items() if not key.startswith('__') and 'id' not in key]
        return separator.join(columns_names)

    def _generate_write_values_string(self, instance: BaseModel) -> str:
        separator = ', '
        instance_attributes = vars(instance)
        db_attributes = [f"'{value}'" for key, value in instance_attributes.items() if
                         not key.startswith('__') and 'id' not in key]
        return separator.join(db_attributes)

    def _generate_update_set_string(self, instance: BaseModel) -> str:
        separator = ', '
        instance_attributes = vars(instance)
        db_attributes = [f"{key} = '{value}'" for key, value in instance_attributes.items() if
                         not key.startswith('__') and 'id' not in key]
        return separator.join(db_attributes)

    def read(self) -> list:
        list_items = []
        query = f'SELECT * FROM {self.table_name}'
        result = self.select_all_query(query)
        for item in result:
            item_instance = self.model(**item)
            list_items.append(item_instance)
        return list_items

    def read_by_id(self, id: int) -> BaseModel:
        query = f"SELECT * FROM {self.table_name} WHERE id = '{id}'"
        result = self.select_one_query(query)
        item_instance = self.model(**result)
        return item_instance

    def write(self, instance: BaseModel) -> None:
        db_attributes_no_id = self._get_db_columns_names_without_id()
        query = f"""
                    INSERT into {self.table_name}({db_attributes_no_id}) 
                    VALUES ({self._generate_write_values_string(instance)})
                """
        self.execute_query(query)

    def update(self, instance: BaseModel) -> None:
        query = f"UPDATE {self.table_name} SET {self._generate_update_set_string(instance)} " \
                f"WHERE id = '{instance.id}'"
        self.execute_query(query)

    def delete(self, id: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = '{id}'"
        self.execute_query(query)
