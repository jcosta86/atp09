from backend.dao.base_dao import BaseDao
from backend.models.category_model import Category


class CategoryDao(BaseDao):
    def __init__(self):
        super().__init__(Category)
