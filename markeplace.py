from historic import save_historic
from global_functions import salva_log_de_uso


# TODO melhorar função produto e marketplace
def set_marketplaces(marketplace: str, description: str):
    marketplace_register = f"'name': {marketplace} 'description': {description}"
    save_historic(marketplace_register, 'logs/marketplaces.txt')
    salva_log_de_uso(f'Salvo marketplace - {marketplace}')
