from backend.dao.base_dao import BaseDao
from backend.models.product_model import Product


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)


def create_table_product():
    query = '''CREATE TABLE IF NOT EXISTS product (
            id serial NOT NULL,
            name varchar(45) NOT NULL,
            description varchar(255) NOT NULL,
            price money NOT NULL,
            CONSTRAINT product_pk PRIMARY KEY (id)
            );
            '''
    ProductDao.execute_query(query)
