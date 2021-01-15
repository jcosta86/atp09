from backend.dao.seller_dao import SellerDao
from backend.controllers.base_controller import BaseController

DAO = SellerDao()

class SellerController(BaseController):
    def __init__(self):
        super().__init__( DAO, 'Seller')

