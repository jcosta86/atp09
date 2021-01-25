from backend.models.marketplace_model import Marketplace


marketplace = Marketplace('Izi', 'Izi izi')
assert type(marketplace) == Marketplace
assert isinstance(marketplace, Marketplace)
assert marketplace.name == 'Izi'
assert marketplace.description == 'Izi izi'
assert type(marketplace.name) == str
assert type(marketplace.description) == str
