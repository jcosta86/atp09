from backend.dao.log_dao import insert_log
from backend.dao.product_dao import write, read


def write_product(name: str, description: str, price: float) -> None:
    write(name, description, price)
    insert_log('Inserted', f'Product - {name}')


def read_product() -> list:
    products = read()
    insert_log('List', 'Product')
    return products
