from backend.controllers.log_controller import write_log
from backend.dao.product_dao import write, read, update, delete
from backend.models.product_model import Product


def write_product(name: str, description: str, price: float) -> None:
    product = Product(name, description, price)
    write(product)
    write_log('Inserted', f'Product - {name}')


def read_product() -> list:
    products = read()
    write_log('List', 'Product')
    return products

def update_product(name: str, description: str, price: float, id: int) -> None:
    product = Product(name, description, price, id)
    update(product)
    write_log("Updated", f"Product - ID: {id}")


def delete_product(id:int) -> None:
    delete(id)
    write_log("Deleted", f"Product - ID: {id}")