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

    def test_validator_blank_name(self) -> None:
        product = Product(self.name, self.description, self.price)
        try:
            product.name = '' 
        except Exception as error:
            assert isinstance(error, ValueError)

    def test_validator_blank_description(self) -> None:
        product = Product(self.name, self.description, self.price)
        try:
            product.description = '' 
        except Exception as error:
            assert isinstance(error, ValueError)


    def test_validator_blank_price(self) -> None:
        product = Product(self.name, self.description, self.price)
        try:
            product.price = '' 
        except Exception as error:
            assert isinstance(error, ValueError)

def start_test_product_model():
    test_product_model = TestProductModel()
    test_product_model.test_atributes()
    test_product_model.test_validator_blank_name()
    test_product_model.test_validator_blank_description()
    test_product_model.test_validator_blank_price()

start_test_product_model()
