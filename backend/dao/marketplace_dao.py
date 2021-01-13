from backend.dao.database import execute_query, select_query
from backend.models.marketplace_model import Marketplace


def create_table_marketplace():
    query = '''CREATE TABLE IF NOT EXISTS marketplace (
                id serial NOT NULL,
                name varchar(45) NOT NULL,
                description varchar(255) NULL,
                CONSTRAINT marketplace_pk PRIMARY KEY (id)
            );
            '''
    execute_query(query)


def write(marketplace: Marketplace) -> None:
    create_table_marketplace()
    query = f"INSERT INTO marketplace (name, description) VALUES ('{marketplace.name}', '{marketplace.description}')"
    execute_query(query)


def read():
    create_table_marketplace()
    list_marketplaces: list = []
    query = f"SELECT name, description FROM marketplace"
    products_tuple = select_query(query)

    for obj in products_tuple:
        marketplace = Marketplace(obj[0], obj[1])
        list_marketplaces.append(marketplace)

    return list_marketplaces
