from backend.dao.base_dao import BaseDao
from backend.models.marketplace_model import Marketplace


class MarketplaceDao(BaseDao):
    def __init__(self):
        super().__init__(Marketplace)

    def create_table(self) -> None:
        query = f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id serial NOT NULL,
                    name varchar(45) NOT NULL,
                    description varchar(255) NULL,
                    CONSTRAINT {self.table_name}_pk PRIMARY KEY (id)
                );
                '''
        self.execute_query(query)
