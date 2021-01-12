from .database import insert_query, select_query

def write(name: str, description: str)-> None:
    query = f"INSERT INTO marketplace (name, description) VALUES ('{name}', '{description}')"
    insert_query(query)


def read():
    list_products: list = []
    query = f"SELECT name, description FROM marketplace"
    products_tuple = select_query(query)

    for obj in products_tuple:
        list_products.append([obj[0],obj[1]])

    return list_products