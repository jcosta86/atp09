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

    def create_table(self) -> None:
        raise NotImplementedError

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

    def _get_primary_key(self) -> str:
        pk_name_query = f"""
                        SELECT column_name FROM information_schema.key_column_usage 
                        WHERE table_name = '{self.table_name}'
                        """
        pk_name = self.select_one_query(pk_name_query)[0]
        return pk_name

    def read(self) -> list:
        list_items = []
        query = f'SELECT * FROM {self.table_name}'
        result = self.select_all_query(query)
        for item in result:
            item_instance = self.model(**item)
            list_items.append(item_instance)
        return list_items

    def read_by_id(self, id: int) -> BaseModel:
        pk_name = self._get_primary_key()
        query = f"SELECT * FROM {self.table_name} WHERE {pk_name} = '{id}'"
        result = self.select_one_query(query)
        item_instance = self.model(**result)
        return item_instance

    def read_by(self, column_name: str, value: any) -> BaseModel:
        query = f"SELECT * FROM {self.table_name} WHERE {column_name} = '{value}'"
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
        pk_name = self._get_primary_key()
        query = f"UPDATE {self.table_name} SET {self._generate_update_set_string(instance)} " \
                f"WHERE {pk_name} = '{instance.id}'"
        self.execute_query(query)

    def delete(self, id: int) -> None:
        pk_name = self._get_primary_key()
        query = f"DELETE FROM {self.table_name} WHERE {pk_name} = '{id}'"
        self.execute_query(query)
