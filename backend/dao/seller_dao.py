from backend.dao.database import select_query, execute_query

def create_table_seller():
    query = '''CREATE TABLE IF NOT EXISTS seller (
            id serial NOT NULL,
            fullname varchar(45) NOT NULL,
            phone int4 NOT NULL,
            email varchar(45) NOT NULL,
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
        list_sellers.append([seller[0],seller[1],seller[2]])
    return list_sellers


def write(fullname: str, email: str, phone: str) -> None:
    create_table_seller()
    query = f"INSERT into seller(fullname, email, phone) VALUES('{fullname}','{email}','{phone}')"
    execute_query(query)
