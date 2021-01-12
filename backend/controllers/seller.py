from backend.dao.log_dao import insert_log
from backend.dao.seller_dao import write, read


def write_seller(fullname: str, email: str, phone: str) -> None:
    write(fullname, email, phone)
    insert_log("Inserted", f"Seller - {fullname}")


def read_seller() -> list:
    sellers = read()
    insert_log("List", "Seller")
    return sellers
