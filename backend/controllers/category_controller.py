from backend.controllers.log_controller import write_log
from backend.dao.category_dao import CategoryDao

from backend.models.category_model import Category

DAO = CategoryDao()


def write_category(name: str, description: str) -> None:
    category = Category(None, name, description)
    DAO.write(category)
    write_log("Inserted", f"Category - {name}")


def read_categories() -> list:
    categories = DAO.read()
    write_log("List", "Category")
    return categories


def update_category(name: str, description: str, id: int) -> None:
    category = Category(id, name, description)
    DAO.update(category)
    write_log("Updated", f"Category - ID: {id}")


def delete_category(id: int) -> None:
    DAO.delete(id)
    write_log("Deleted", f"Category - ID: {id}")
