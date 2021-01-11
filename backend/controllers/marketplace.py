from ..dao.dao_txt.marketplace_dao_txt import *
from ..utils.utils import save_logfile


def write_marketplace(name: str, description: str) -> None:
    write(name, description)
    save_logfile(f'Inserted - Marketplace - {name}')


def read_marketplace() -> list:
    marketplaces = read()
    print(marketplaces)
    save_logfile(f'List - Marketplace')
    return marketplaces
