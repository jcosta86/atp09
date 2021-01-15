from backend.controllers.log_controller import write_log
from backend.dao.marketplace_dao import MarketplaceDao
from backend.models.marketplace_model import Marketplace

DAO = MarketplaceDao()


def write_marketplace(name: str, description: str) -> None:
    marketplace = Marketplace(name, description)
    DAO.write(marketplace)
    write_log("Inserted", f"Marketplace - {name}")


def read_marketplace() -> list:
    marketplaces = DAO.read()
    write_log('List', 'Marketplace')
    return marketplaces


def update_marketplace(id: int, name: str, description: str) -> None:
    marketplace = Marketplace(id=id, name=name, description=description)
    DAO.update(marketplace)
    write_log("Updated", f"Marketplace - ID: {id}")


def delete_marketplace(id: int) -> None:
    DAO.delete(id)
    write_log("Deleted", f"Marketplace - ID: {id}")
