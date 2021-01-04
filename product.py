from historic import save_historic
from global_functions import salva_log_de_uso


# TODO melhorar função produto e marketplace
def set_product(product_name: str, description: str, price: float):
    product_register = f"'name': {product_name}, 'description': {description}, 'price': {price}"
    save_historic(product_register, 'logs/products.txt')
    salva_log_de_uso(f'Salvo produto - {product_name}')
