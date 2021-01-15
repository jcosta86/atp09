from backend.dao.base_dao import BaseDao
from backend.models.marketplace_model import Marketplace


class MarketplaceDao(BaseDao):
    def __init__(self):
        super().__init__(Marketplace)


def create_table_marketplace():
    query = '''CREATE TABLE IF NOT EXISTS marketplace (
                id serial NOT NULL,
                name varchar(45) NOT NULL,
                description varchar(255) NULL,
                CONSTRAINT marketplace_pk PRIMARY KEY (id)
            );
            '''
    MarketplaceDao.execute_query(query)
