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
    query = f"INSERT INTO marketplace (name, description) VALUES ('{marketplace.name}', '{marketplace.description}');"
    execute_query(query)


def read():
    list_marketplaces: list = []
    query = f"SELECT id, name, description FROM marketplace;"
    products_tuple = select_query(query)

    for obj in products_tuple:
        marketplace = Marketplace(name=obj[1], description=obj[2], id=obj[0])
        list_marketplaces.append(marketplace)

    return list_marketplaces


def update(marketplace: Marketplace):
    query = f"""
            UPDATE marketplace SET name = '{marketplace.name}', description = '{marketplace.description}' 
            WHERE id = {marketplace.id};
            """
    execute_query(query)


def delete(id: int):
    query = f"DELETE FROM marketplace WHERE id = {id};"
    execute_query(query)
