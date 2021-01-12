from backend.controllers.log import create_log
from backend.dao.product_dao import write, read


def write_product(name: str, description: str, price: float) -> None:
    write(name, description, price)
    create_log('Inserted', f'Product - {name}')


def read_product() -> list:
    products = read()
    create_log('List', 'Product')
    return products
