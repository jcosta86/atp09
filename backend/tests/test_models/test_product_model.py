import sys
sys.path.append('.')

from backend.models.product_model import Product


class TestProductModel:
    name = 'Produto Bom'
    description = 'Muito bom'
    price = 77.50
    
    def test_atributes(self) -> None:
        product = Product(self.name, self.description, self.price)
        assert isinstance(product, Product)
        assert product.name is self.name
        assert product.description is self.description
        assert product.price is self.price

def start_test_product_model():
    test_product_model = TestProductModel()
    test_product_model.test_atributes()

start_test_product_model()
