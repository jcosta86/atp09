from backend.dao.base_dao import BaseDao
from backend.models.product_model import Product


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)

    def read_all(self) -> list:
        result = super().read_all()
        for product in result:
            product.price = product.price.strip('$').replace(',', '')
            product.price = float(product.price)
        return result
    
    def read_by_id(self, id: int) -> Product:
        product = super().read_by_id(id)
        product.price = product.price.strip('$').replace(',', '')
        product.price = float(product.price)
        return product
