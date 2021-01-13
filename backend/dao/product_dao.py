from backend.dao.database import execute_query, select_query
from backend.models.product_model import Product


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


def write(product: Product) -> None:
    create_table_product()
    query = f"INSERT INTO product (name, description, price) VALUES ('{product.name}', '{product.description}', '{product.price}')"
    execute_query(query)


def read():
    create_table_product()
    list_products: list = []
    query = f"SELECT name, description, price, id FROM product"
    select = select_query(query)

    for item in select:
        product = Product(item[0], item[1], float(item[2].strip('$').replace(',','')), item[3])
        list_products.append(product)

    return list_products


def update(product: Product) -> None:
    query = f"UPDATE product SET name = '{product.name}', description = '{product.description}', price = '{product.price}' WHERE id = '{product.id}'"
    execute_query(query)


def delete(id: int) -> None:
    query = f"DELETE FROM product WHERE id = '{id}'"
    execute_query(query)
