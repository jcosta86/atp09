from backend.controllers.log import create_log
from backend.dao.product_dao import write, read
from backend.models.product import Product


<<<<<<< HEAD
def write_product(name: str, description, price: float) -> None:
    product = Product(name, description, price)
    write(product)
    insert_log('Inserted', f'Product - {name}')
=======

def write_product(product: Product) -> None:
    write(product)
    create_log('Inserted', f'Product - {name}')
>>>>>>> 74fc270c90dd064fda6d80fb693bcf17680dd386


def read_product() -> list:
    products = read()
    create_log('List', 'Product')
    return products
