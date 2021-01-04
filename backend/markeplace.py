from backend.historic import save_in_database
from backend.global_functions import save_log


# TODO melhorar função produto e marketplace
def set_marketplaces(marketplace: str, description: str) -> None:
    marketplace_register = f"'name': {marketplace} 'description': {description}"
    save_in_database(marketplace_register, 'logs/marketplaces.txt')
    save_log(f'Salvo marketplace - {marketplace}')
