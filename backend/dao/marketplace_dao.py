from .database import execute_query, select_query

def create_table_marketplace():
    query = '''CREATE TABLE IF NOT EXISTS marketplace (
                id serial NOT NULL,
                name varchar(45) NOT NULL,
                description varchar(255) NULL,
                CONSTRAINT marketplace_pk PRIMARY KEY (id)
            );
            '''
    execute_query(query)


def write(name: str, description: str)-> None:
    create_table_marketplace()
    query = f"INSERT INTO marketplace (name, description) VALUES ('{name}', '{description}')"
    execute_query(query)


def read():
    create_table_marketplace()
    list_products: list = []
    query = f"SELECT name, description FROM marketplace"
    products_tuple = select_query(query)

    for obj in products_tuple:
        list_products.append([obj[0],obj[1]])

    return list_products