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


menu = [
    {'name': 'Marketplaces',
     'route': '/marketplaces'},
    {'name': 'Produtos',
     'route': '/products'},
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