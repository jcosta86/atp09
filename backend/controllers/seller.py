from ..dao.seller_dao import *
from ..utils.utils import save_logfile


def write_seller(fullname: str, email: str, phone: str) -> None:
    write(fullname, email, phone)
    #save_logfile(f'Inserted - Seller - {fullname}')


def read_seller() -> list:
    sellers = read()
    #save_logfile(f'List - Seller')
    return sellers
