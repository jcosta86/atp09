from backend.dao.base_dao import BaseDao
from backend.models.marketplace_model import Marketplace


class MarketplaceDao(BaseDao):
    def __init__(self):
        super().__init__(Marketplace)
