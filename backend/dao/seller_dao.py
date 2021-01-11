from backend.dao.database import select_query, insert_query


def read() -> list:
    list_sellers = []
    query = "SELECT fullname, email, phone FROM seller"
    select = select_query(query)
    for seller in select:
        list_sellers.append([seller[0],seller[1],seller[2]])
    return list_sellers


def write(fullname: str, email: str, phone: str) -> None:
    query = f"INSERT into seller(fullname, email, phone) VALUES('{fullname}','{email}','{phone}')"
    insert_query(query)
