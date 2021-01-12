from backend.controllers.log import create_log
from backend.dao.product_dao import write, read
from backend.models.product import Product



def write_product(product: Product) -> None:
    write(product)
    create_log('Inserted', f'Product - {name}')


def read_product() -> list:
    products = read()
    create_log('List', 'Product')
    return products
