from ..utils.utils import save_logfile
from ..dao.product_dao import *


def write_product(name: str, description: str, price: float) -> None:
    write(name, description, price)
    save_logfile('Inserted',  f'Product - {name}')


def read_product() -> list:
    products = read()
    save_logfile('List', 'Product')
    return products
