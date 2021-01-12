from ..dao.log_dao import insert_log
from ..dao.seller_dao import *
from ..utils.utils import save_logfile


def write_seller(fullname: str, email: str, phone: str) -> None:
    write(fullname, email, phone)
    insert_log("Inserted", f"Seller - {fullname}")
    #save_logfile(f'Inserted - Seller - {fullname}')


def read_seller() -> list:
    sellers = read()
    insert_log("Inserted", "Seller")
    #save_logfile(f'List - Seller')
    return sellers
