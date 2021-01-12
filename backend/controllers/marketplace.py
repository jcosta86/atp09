from backend.controllers.log import create_log
from backend.dao.marketplace_dao import write, read
from backend.models.marketplace import Marketplace


def write_marketplace(name: str, description: str) -> None:
    marketplace = Marketplace(name, description)
    write(marketplace)
    create_log("Inserted", f"Marketplace - {name}")


def read_marketplace() -> list:
    marketplaces = read()
    create_log('List', 'Marketplace')
    return marketplaces
