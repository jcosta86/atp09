from backend.dao.log_dao import insert_log
from backend.dao.product_dao import write, read
from backend.models.product import Product


def write_product(product: Product) -> None:
    write(product)
    insert_log('Inserted', f'Product - {product.name}')


def read_product() -> list:
    products = read()
    insert_log('List', 'Product')
    return products
