from .database import insert_query, select_query

def insert_product(name: str, description: str, price: float)-> None:
    query = f"INSERT INTO product (name, description, price) VALUES ('{name}', '{description}', '{price}')"
    insert_query(query)


def select_product():
    list_products: list = []
    query = f"SELECT name, description, price FROM product"
    products_tuple = select_query(query)

    for obj in products_tuple:
        list_products.append([obj[0],obj[1],obj[2]])

    return list_products