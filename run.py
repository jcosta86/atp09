from dotenv import load_dotenv

from backend.controllers.category_controller import DAO as CATEGORY
from backend.controllers.log_controller import DAO as LOG
from backend.controllers.marketplace_controller import DAO as MARKETPLACE
from backend.controllers.product_controller import DAO as PRODUCT
from backend.controllers.seller_controller import DAO as SELLER
from backend.tests.test_controller.test_base_controller import start_base_controller_tests
from backend.tests.test_dao.test_base_dao import start_test_base_dao
from backend.tests.test_models.test_category_model import start_test_category_model
from backend.tests.test_models.test_log_model import start_test_log
from backend.tests.test_models.test_marketplace_model import start_test_marketplace_model
from backend.tests.test_models.test_product_model import start_test_product_model
from backend.tests.test_models.test_seller_model import start_test_seller_model


from frontend.web import app


def create_tables():
    CATEGORY.create_table()
    LOG.create_table()
    SELLER.create_table()
    MARKETPLACE.create_table()
    PRODUCT.create_table()
    

def run_tests():
    start_base_controller_tests()
    start_test_base_dao()
    start_test_category_model()
    start_test_log()
    start_test_marketplace_model()
    start_test_product_model()
    start_test_seller_model()

if __name__ == "__main__":
    load_dotenv()
    run_tests()
    app.run(debug=True)
    create_tables()
