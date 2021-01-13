from backend.controllers.log_controller import write_log
from backend.dao.category_dao import read, write, update, delete

from backend.models.category_model import Category


def write_category(name: str, description: str) -> None:
    category = Category(name, description)
    write(category)
    write_log("Inserted", f"Category - {name}")


def read_categories() -> list:
    categories = read()
    write_log("List", "Category")
    return categories


def update_category(name: str, description: str, id: int) -> None:
    category = Category(name, description, id)
    update(category)
    write_log("Updated", "Category")


def delete_category(id:int) -> None:
    delete(id)