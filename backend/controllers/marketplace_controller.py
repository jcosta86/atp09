from backend.dao.marketplace_dao import MarketplaceDao 
from backend.controllers.base_controller import BaseController

DAO = MarketplaceDao()

class MarketplaceController(BaseController):
    def __init__(self):
        super().__init__( DAO, 'Marketplace')
