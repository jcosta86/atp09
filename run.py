from dotenv import load_dotenv

from backend.dao.category_dao import create_table_category
from backend.dao.log_dao import create_table_logfile
from backend.dao.marketplace_dao import create_table_marketplace
from backend.dao.product_dao import create_table_product
from backend.dao.seller_dao import create_table_seller
from frontend.web import app


def create_tables():
    create_table_logfile()
    create_table_seller()
    create_table_marketplace()
    create_table_category()
    create_table_product()


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)
    create_tables()
