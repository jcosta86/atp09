import sys
sys.path.append('../app')

from datetime import datetime

from backend.historic import save_in_database

def save_log(log_name: str) -> None:
    """
    Saves system logs
    :param log_name:
    :return: None
    """
    current_datetime = datetime.now()
    current_formated_datetime = current_datetime.strftime('%d/%m/%Y %H:%M:%S')
    log_line = f'log: {log_name} - Data e hora: {current_formated_datetime}'
    save_in_database(log_line, 'logs/historico_log.txt')


def read_marketplaces() -> list:
    marketplaces: list = []
    archive = open('logs/marketplaces.txt', 'r')
  
    for obj in archive:
        line_cleaned = obj.strip() # retira caracteres de escape e espacos branco (\n \t \r ' ')
        data_line = line_cleaned.split('"') # transforma a string em uma lista de acordo com o caracter passado como argumento
        formated_line = {data_line[1]: data_line[3], data_line[5]: data_line[7]}
        marketplaces.append(formated_line)
    
    archive.close()
    return marketplaces


def read_products() -> list:
    products: list = []
    archive = open('logs/products.txt', 'r')

    for obj in archive:
        line_cleaned = obj.strip()  # clear caracteres and clear white spaces (\n \t \r ' ')
        data_line = line_cleaned.split('"')
        formated_line = {data_line[1]: data_line[3], data_line[5]: data_line[7], data_line[9]: data_line[11]}
        products.append(formated_line)

    archive.close()
    return products


def read_categories() -> list:
    categories: list = []
    archive = open('logs/categories.txt', 'r')

    for obj in archive:
        line_cleaned = obj.strip()  # clear caracteres and clear white spaces (\n \t \r ' ')
        data_line = line_cleaned.split('"')
        formated_line = {data_line[1]: data_line[3], data_line[5]: data_line[7]}
        categories.append(formated_line)

    archive.close()
    return categories

def read_sellers() -> list:
    sellers: list = []
    archive = open('logs/sellers.txt', 'r')

    for obj in archive:
        line_cleaned = obj.strip()  # clear caracteres and clear white spaces (\n \t \r ' ')
        data_line = line_cleaned.split('"')
        formated_line = {data_line[1]: data_line[3], data_line[5]: data_line[7], data_line[9]: data_line[11]}
        sellers.append(formated_line)

    archive.close()
    return sellers


menu = [
    {'name': 'Marketplaces',
     'route': '/marketplaces'},
    {'name': 'Produtos',
     'route': '/products'},
    {'name': 'Categorias',
     'route': '/categories'},
    {'name': 'Vendedores',
     'route': '/sellers'},
     {'name': 'Listar Marketplace',
     'route': '/list_marketplaces'},
    {'name': 'Listar Produtos',
     'route': '/list_products'},
    {'name': 'Listar Categorias',
     'route': '/list_categories'},
    {'name': 'Listar Vendedores',
     'route': '/list_sellers'},
    {'name': 'Log de uso',
     'route': '/historico'}
]

links = [
    {
        'route': '/',
        'name': 'Voltar'
    },
    {
        'route': 'http://www.olist.com',
        'name': 'olist'
    }
]
