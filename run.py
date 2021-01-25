from dotenv import load_dotenv

from backend.controllers.category_controller import DAO as CATEGORY
from backend.controllers.log_controller import DAO as LOG
from backend.controllers.marketplace_controller import DAO as MARKETPLACE
from backend.controllers.product_controller import DAO as PRODUCT
from backend.controllers.seller_controller import DAO as SELLER
from frontend.web import app


def create_tables():
    CATEGORY.create_table()
    LOG.create_table()
    SELLER.create_table()
    MARKETPLACE.create_table()
    PRODUCT.create_table()


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)
    create_tables()
