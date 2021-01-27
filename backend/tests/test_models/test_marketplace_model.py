import sys
sys.path.append('.')
from backend.models.marketplace_model import Marketplace


class TestMarketplaceModel:
    marketplace_name = 'marketplace'
    marketplace_description = 'marketplace description'
    marketplace_id = 8

    def test_atributes(self) -> None:
        marketplace = Marketplace(self.marketplace_name, self.marketplace_description, self.marketplace_id)
        assert isinstance(marketplace, Marketplace)
        assert marketplace.name is self.marketplace_name
        assert marketplace.description is self.marketplace_description
        assert marketplace.id is self.marketplace_id

    def test_validator_blank_name(self) -> None:
        marketplace = Marketplace(self.marketplace_name, self.marketplace_description)
        try:
            marketplace.name = '' 
        except Exception as error:
            assert isinstance(error, ValueError)

def start_test_marketplace_model():
    test_marketplace_model = TestMarketplaceModel()
    test_marketplace_model.test_atributes()
    test_marketplace_model.test_validator_blank_name()


start_test_marketplace_model()
