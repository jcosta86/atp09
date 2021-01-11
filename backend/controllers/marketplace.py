from ..dao.log_dao import insert_log
from ..utils.utils import save_logfile
from ..dao.marketplace_dao import *


def write_marketplace(name: str, description: str) -> None:
    write(name, description)
    insert_log("Inserted", f"Marketplace - {name}")
    #save_logfile(f'Inserted - Marketplace - {name}')


def read_marketplace() -> list:
    marketplaces = read()
    insert_log('List', 'Marketplace')
    return marketplaces
