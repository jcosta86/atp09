from backend.models.category_model import Category
from backend.models.base_model import BaseModel


class TestCategoryModel:
    category_name = 'alguma coisa'
    category_description = 'description category'
    category_id = 25

    def test_constructor(self) -> None:
        category = Category(self.category_name, self.category_description, self.category_id)
        assert isinstance(category, Category)
        assert isinstance(category, BaseModel)
        assert category.name is self.category_name
        assert category.description is self.category_description
        assert category.id is self.category_id
    
    def test_validator_blank_name(self) -> None:
        category = Category(self.category_name, self.category_description)
        try:
            category.name = '' 
        except Exception as error:
            assert isinstance(error, ValueError)


def start_test_category_model():
    test_category_model = TestCategoryModel()
    test_category_model.test_constructor()
    test_category_model.test_validator_blank_name()


start_test_category_model()
