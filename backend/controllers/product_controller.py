from backend.dao.product_dao import ProductDao
from backend.controllers.base_controller import BaseController

DAO = ProductDao()

class ProductController(BaseController):
    def __init__(self):
        super().__init__( DAO, 'Product')