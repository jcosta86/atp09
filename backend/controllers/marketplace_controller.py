from backend.controllers.log_controller import write_log
from backend.dao.marketplace_dao import write, read
from backend.models.marketplace_model import Marketplace


def write_marketplace(name: str, description: str) -> None:
    marketplace = Marketplace(name, description)
    write(marketplace)
    write_log("Inserted", f"Marketplace - {name}")


def read_marketplace() -> list:
    marketplaces = read()
    write_log('List', 'Marketplace')
    return marketplaces
