from backend.controllers.log import create_log
from backend.dao.seller_dao import write, read
from backend.models.seller import Seller


def write_seller(fullname: str, email: str, phone: str) -> None:
    seller = Seller(fullname, email, phone)
    write(seller)
    create_log("Inserted", f"Seller - {seller.fullname}")


def read_seller() -> list:
    sellers = read()
    create_log("List", "Seller")
    return sellers
