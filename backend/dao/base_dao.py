from backend.dao.database import select_query, execute_query
from backend.models.base_model import BaseModel


class BaseDao:
    def __init__(self, model: type(BaseModel)):
        self.model = model
        self.table_name = self.model.__tablename__

    def _get_db_attributes_names(self) -> str:
        separator = ', '
        model_attributes = vars(self.model)
        db_attributes = [key for key, value in model_attributes.items() if not key.startswith('__')]
        return separator.join(db_attributes)

    def _get_db_attributes_names_without_id(self) -> str:
        separator = ', '
        model_attributes = vars(self.model)
        db_attributes = [key for key, value in model_attributes.items() if not key.startswith('__') and 'id' not in key]
        return separator.join(db_attributes)

    def _generate_write_values_string(self, instance) -> str:
        separator = ', '
        model_attributes = vars(instance)
        db_attributes = [f"'{value}'" for key, value in model_attributes.items() if
                         not key.startswith('__') and 'id' not in key]
        return separator.join(db_attributes)

    def _generate_update_set_string(self, instance) -> str:
        separator = ', '
        model_attributes = vars(instance)
        db_attributes = [f"{key} = '{value}'" for key, value in model_attributes.items() if
                         not key.startswith('__') and 'id' not in key]
        return separator.join(db_attributes)

    def read(self) -> list:
        db_attributes = self._get_db_attributes_names()
        list_items = []
        query = f'SELECT {db_attributes} FROM {self.table_name}'
        result = select_query(query)
        for item in result:
            item = list(item)
            id = item.pop(0)
            item_instance = self.model(*item, id)
            list_items.append(item_instance)
        return list_items

    def write(self, instance) -> None:
        db_attributes_no_id = self._get_db_attributes_names_without_id()
        query = f"""
                    INSERT into {self.table_name}({db_attributes_no_id}) 
                    VALUES ({self._generate_write_values_string(instance)})
                """
        execute_query(query)

    def update(self, instance) -> None:
        query = f"UPDATE {self.table_name} SET {self._generate_update_set_string(instance)} " \
                f"WHERE id = '{instance.id}'"
        execute_query(query)

    def delete(self, id: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = '{id}'"
        execute_query(query)
