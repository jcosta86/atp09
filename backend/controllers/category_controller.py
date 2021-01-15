from backend.dao.category_dao import CategoryDao
from backend.controllers.base_controller import BaseController

DAO = CategoryDao()

class CategoryController(BaseController):
    def __init__(self):
        super().__init__( DAO, 'Category')


