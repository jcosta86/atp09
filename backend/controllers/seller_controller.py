from backend.controllers.log_controller import write_log
from backend.dao.seller_dao import SellerDao
from backend.models.seller_model import Seller

DAO = SellerDao()


def write_seller(fullname: str, email: str, phone: str) -> None:
    seller = Seller(fullname, email, phone)
    DAO.write(seller)
    write_log("Inserted", f"Seller - {seller.fullname}")


def read_seller() -> list:
    sellers = DAO.read()
    write_log("List", "Seller")
    return sellers


def update_seller(id: int, fullname: str, email: str, phone: str) -> None:
    seller = Seller(id=id, fullname=fullname, email=email, phone=phone)
    DAO.update(seller)
    write_log("Updated", f"Seller - ID: {id}")


def delete_seller(id: int) -> None:
    DAO.delete(id)
    write_log("Deleted", f"Seller - ID: {id}")
