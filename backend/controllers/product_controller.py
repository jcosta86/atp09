from backend.controllers.log_controller import write_log
from backend.dao.product_dao import ProductDao
from backend.models.product_model import Product

DAO = ProductDao()


def write_product(name: str, description: str, price: float) -> None:
    product = Product(name, description, price)
    DAO.write(product)
    write_log('Inserted', f'Product - {name}')


def read_product() -> list:
    products = DAO.read()
    write_log('List', 'Product')
    return products


def update_product(name: str, description: str, price: float, id: int) -> None:
    product = Product(name, description, price, id)
    DAO.update(product)
    write_log("Updated", f"Product - ID: {id}")


def delete_product(id: int) -> None:
    DAO.delete(id)
    write_log("Deleted", f"Product - ID: {id}")
