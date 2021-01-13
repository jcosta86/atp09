from backend.dao.database import select_query, execute_query
from backend.models.seller_model import Seller


def create_table_seller():
    query = '''CREATE TABLE IF NOT EXISTS seller (
            id serial NOT NULL,
            fullname varchar NOT NULL,
            phone varchar NOT NULL,
            email varchar NOT NULL,
            CONSTRAINT seller_pk PRIMARY KEY (id)
            );
            '''
    execute_query(query)


def read() -> list:
    list_sellers = []
    query = "SELECT id, fullname, email, phone FROM seller"
    select = select_query(query)
    for seller in select:
        seller = Seller(id=seller[0], fullname=seller[1], email=seller[2], phone=seller[3])
        list_sellers.append(seller)
    return list_sellers


def write(seller: Seller) -> None:
    query = f"INSERT into seller(fullname, email, phone) VALUES('{seller.fullname}','{seller.email}','{seller.phone}')"
    execute_query(query)


def update(seller: Seller):
    query = f"""
            UPDATE seller SET fullname = '{seller.fullname}', email = '{seller.email}', phone = '{seller.phone}'
            WHERE id = {seller.id}
            """
    execute_query(query)


def delete(id: int):
    query = f"DELETE FROM seller WHERE id = {id}"
    execute_query(query)
