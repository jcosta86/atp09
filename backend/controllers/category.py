from ..dao.category_dao import read, write
from ..dao.log_dao import insert_log
from ..utils.utils import save_logfile


def write_category(name: str, description: str) -> None:
    write(name, description)
    #save_logfile(f'Inserted - Category - {name}')
    insert_log("Inserted", f"Category - {name}")


def read_categories() -> list:
    categories = read()
    #save_logfile(f'List - Category')
    insert_log("List", "Category")
    return categories
