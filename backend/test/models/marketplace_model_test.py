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


def start_test_marketplace_model():
    test_marketplace_model = TestMarketplaceModel()
    test_marketplace_model.test_atributes()


start_test_marketplace_model()
