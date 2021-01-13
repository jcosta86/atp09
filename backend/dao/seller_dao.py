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
    create_table_seller()
    list_sellers = []
    query = "SELECT fullname, email, phone FROM seller"
    select = select_query(query)
    for seller in select:
        seller = Seller(seller[0], seller[1], seller[2])
        list_sellers.append(seller)
    return list_sellers


def write(seller: Seller) -> None:
    create_table_seller()
    query = f"INSERT into seller(fullname, email, phone) VALUES('{seller.fullname}','{seller.email}','{seller.phone}')"
    execute_query(query)
