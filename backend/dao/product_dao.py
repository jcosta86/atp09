from backend.dao.base_dao import BaseDao
from backend.models.product_model import Product


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)

    def create_table(self) -> None:
        query = f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
                id serial NOT NULL,
                name varchar(45) NOT NULL,
                description varchar(255) NOT NULL,
                price money NOT NULL,
                CONSTRAINT {self.table_name}_pk PRIMARY KEY (id)
                );
                '''
        self.execute_query(query)

    def read(self) -> list:
        result = super().read()
        for product in result:
            product.price = product.price.strip('$').replace(',', '')
            product.price = float(product.price)
        return result
