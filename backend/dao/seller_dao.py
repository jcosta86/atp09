import sys
sys.path.append('.')

from backend.dao.base_dao import BaseDao
from backend.models.seller_model import Seller


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)

