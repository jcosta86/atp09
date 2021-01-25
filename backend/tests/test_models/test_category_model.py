from backend.models.category_model import Category
from backend.models.base_model import BaseModel


class TestCategoryModel:
    category_name = 'name category'
    category_description = 'description category'
    category_id = 25

    def test_constructor(self) -> None:
        category = Category(self.category_name, self.category_description, self.category_id)
        assert isinstance(category, Category)
        assert isinstance(category, BaseModel)
        assert category.name is self.category_name
        assert category.description is self.category_description
        assert category.id is self.category_id


def start_test_category_model():
    test_category_model = TestCategoryModel()
    test_category_model.test_constructor()


start_test_category_model()
