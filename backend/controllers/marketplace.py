from backend.dao.log_dao import insert_log
from backend.dao.marketplace_dao import write, read


def write_marketplace(name: str, description: str) -> None:
    write(name, description)
    insert_log("Inserted", f"Marketplace - {name}")


def read_marketplace() -> list:
    marketplaces = read()
    insert_log('List', 'Marketplace')
    return marketplaces
