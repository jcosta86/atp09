from ..dao.dao_txt.product_dao_txt import *
from ..utils.utils import save_logfile
from ..dao.product_dao import insert_product, select_product

def write_product(name: str, description: str, price: float) -> None:
    #write(name, description, price)
    insert_product(name, description, price)
    save_logfile(f'Inserted - Product - {name}')


def read_product() -> list:
    #products = read()
    products = select_product()
    save_logfile(f'List - Product')
    return products