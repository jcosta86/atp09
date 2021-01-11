from ..dao.dao_txt.marketplace_dao_txt import *
from ..utils.utils import save_logfile
from ..dao.marketplace_dao import insert_marketplace, select_marketplace

def write_marketplace(name: str, description: str) -> None:
    #write(name, description) #Use txt function
    insert_marketplace(name, description) #Use Database
    save_logfile(f'Inserted - Marketplace - {name}')


def read_marketplace() -> list:
    #marketplaces = read() #Use txt function
    marketplaces = select_marketplace() #Use Database
    save_logfile(f'List - Marketplace')
    return marketplaces