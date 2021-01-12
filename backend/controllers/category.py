from backend.dao.category_dao import read, write
from backend.dao.log_dao import insert_log
from backend.models.category import Category


def write_category(name: str, description: str) -> None:
    category = Category(name, description)
    write(category)
    insert_log("Inserted", f"Category - {name}")


def read_categories() -> list:
    categories = read()
    insert_log("List", "Category")
    return categories
