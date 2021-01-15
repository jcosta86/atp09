from backend.dao.base_dao import BaseDao
from backend.models.base_model import BaseModel
from backend.models.log_model import Log


class LogDao(BaseDao):
    def __init__(self):
        super().__init__(Log)

    def create_table(self) -> None:
        query = f''' CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id serial NOT NULL,
                    date_activity date NOT NULL,
                    time_activity time NOT NULL,
                    activity varchar(500) NOT NULL,
                    domain_activity varchar(500) NOT NULL,
                    CONSTRAINT {self.table_name}_pk PRIMARY KEY (id)
                );
                '''
        self.execute_query(query)

    def update(self, instance: BaseModel) -> None:
        raise NotImplementedError
