import sys
sys.path.append('.')

from backend.controllers.base_controller import BaseController
from backend.models.marketplace_model import Marketplace
from backend.dao.marketplace_dao import MarketplaceDao
from backend.dao.session import Session


class TestBaseController:
    marketplace_dao = MarketplaceDao()
    base_controller = BaseController(marketplace_dao, 'marketplace')
    name = 'testandooo'
    description = 'Test Marketplace Controller'
    id = None
    
    def test_save(self) -> None:
        mkt = Marketplace(self.name, self.description)
        self.base_controller.write(mkt)
        r = self.base_controller.read()[-1]
        assert self.name == r.name
        self.id = r.id

    def test_read_all(self) -> None:
        marketplaces = self.base_controller.read()
        assert isinstance(marketplaces, list)
        
    def test_read_by_id(self) -> None:
        marketplace = self.base_controller.read_by_id(self.id)
        assert marketplace.id == self.id
        assert isinstance(marketplace, Marketplace)
    
    def test_update(self) -> None:
        marketplace = self.base_controller.read_by_id(self.id)
        description = marketplace.description
        marketplace.description = 'Test Update Marketplace controller'
        self.base_controller.update(marketplace)
        marketplace_ = self.base_controller.read_by_id(self.id)
        assert marketplace_.description != description

    def test_delete(self) -> None:
        marketplace = self.base_controller.read_by_id(self.id)
        self.base_controller.delete(marketplace)
        marketplace_after_delete = self.base_controller.read_by_id(self.id)
        assert marketplace_after_delete is None
        
def start_base_controller_tests() -> None:
    test_controller = TestBaseController()
    test_controller.test_save()
    test_controller.test_read_all()       
    test_controller.test_read_by_id()       
    test_controller.test_update()       
    test_controller.test_delete()
    
start_base_controller_tests()