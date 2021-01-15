from backend.dao.base_dao import BaseDao
from backend.models.seller_model import Seller


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)


def create_table_seller():
    query = '''CREATE TABLE IF NOT EXISTS seller (
            id serial NOT NULL,
            fullname varchar NOT NULL,
            phone varchar NOT NULL,
            email varchar NOT NULL,
            CONSTRAINT seller_pk PRIMARY KEY (id)
            );
            '''
    SellerDao.execute_query(query)
