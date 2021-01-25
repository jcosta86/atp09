from backend.dao.marketplace_dao import MarketplaceDao 
from backend.controllers.base_controller import BaseController


class MarketplaceController(BaseController):
    def __init__(self) -> None:
        self.__dao = MarketplaceDao()
        super().__init__(self.__dao, 'Marketplace')    

