from backend.controllers.log_controller import write_log
from backend.dao.seller_dao import write, read
from backend.models.seller_model import Seller


def write_seller(fullname: str, email: str, phone: str) -> None:
    seller = Seller(fullname, email, phone)
    write(seller)
    write_log("Inserted", f"Seller - {seller.fullname}")


def read_seller() -> list:
    sellers = read()
    write_log("List", "Seller")
    return sellers
