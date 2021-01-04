from backend.historic import save_in_database
from backend.global_functions import save_log


# TODO melhorar função produto e marketplace
def set_product(product_name: str, description: str, price: float):
    product_register = f"'name': {product_name}, 'description': {description}, 'price': {price}"
    save_in_database(product_register, 'logs/products.txt')
    save_log(f'Salvo produto - {product_name}')
