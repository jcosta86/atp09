from backend.controllers.log_controller import write_log
from backend.dao.seller_dao import write, read, update, delete
from backend.models.seller_model import Seller


def write_seller(fullname: str, email: str, phone: str) -> None:
    seller = Seller(fullname, email, phone)
    write(seller)
    write_log("Inserted", f"Seller - {seller.fullname}")


def read_seller() -> list:
    sellers = read()
    write_log("List", "Seller")
    return sellers


def update_seller(id: int, fullname: str, email: str, phone: str) -> None:
    seller = Seller(id=id, fullname=fullname, email=email, phone=phone)
    update(seller)
    write_log("Updated", f"Seller - ID: {id}")


def delete_seller(id: int) -> None:
    delete(id)
    write_log("Deleted", f"Seller - ID: {id}")
