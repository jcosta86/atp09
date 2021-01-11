from ..dao.dao_txt.category_dao_txt import read, write
from ..utils.utils import save_logfile

def write_category(name: str, description: str) -> None:
    write(name, description)
    save_logfile(f'Inserted - Category - {name}')


def read_categories() -> list:
    categories = read()
    save_logfile(f'List - Category')
    return categories
