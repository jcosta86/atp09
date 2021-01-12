from backend.dao.database import execute_query, select_query


def create_table_product():
    query = '''CREATE TABLE IF NOT EXISTS product (
            id serial NOT NULL,
            name varchar(45) NOT NULL,
            description varchar(255) NOT NULL,
            price money NOT NULL,
            CONSTRAINT product_pk PRIMARY KEY (id)
            );
            '''
    execute_query(query)


def write(name: str, description: str, price: float) -> None:
    create_table_product()
    query = f"INSERT INTO product (name, description, price) VALUES ('{name}', '{description}', '{price}')"
    execute_query(query)


def read():
    create_table_product()
    list_products: list = []
    query = f"SELECT name, description, price FROM product"
    products_tuple = select_query(query)

    for obj in products_tuple:
        list_products.append([obj[0], obj[1], obj[2]])

    return list_products
