from backend.dao.base_dao import BaseDao
from backend.models.seller_model import Seller


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)

    def create_table(self) -> None:
        query = f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
                id serial NOT NULL,
                fullname varchar NOT NULL,
                phone varchar NOT NULL,
                email varchar NOT NULL,
                CONSTRAINT {self.table_name}_pk PRIMARY KEY (id)
                );
                '''
        self.execute_query(query)
