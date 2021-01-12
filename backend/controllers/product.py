from ..utils.utils import save_logfile
from ..dao.product_dao import *
from ..dao.log_dao import insert_log


def write_product(name: str, description: str, price: float) -> None:
    write(name, description, price)
    insert_log('Inserted',  f'Product - {name}')


def read_product() -> list:
    products = read()
    #save_logfile('List', 'Product')
    insert_log('List', 'Product')
    return products
