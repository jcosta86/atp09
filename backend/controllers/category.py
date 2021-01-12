from backend.controllers.log import create_log
from backend.dao.category_dao import read, write

from backend.models.category import Category


def write_category(category: Category) -> None:
    write(category)
    create_log("Inserted", f"Category - {name}")


def read_categories() -> list:
    categories = read()
    create_log("List", "Category")
    return categories
