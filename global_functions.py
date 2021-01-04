from datetime import datetime

from historic import save_historic


def salva_log_de_uso(nome_log: str) -> None:
    data_e_hora_atual = datetime.now()
    data_e_hora = data_e_hora_atual.strftime('%d/%m/%Y %H:%M:%S')
    linha_de_log = f'log: {nome_log} - Data e hora: {data_e_hora}'
    save_historic(linha_de_log, 'logs/historico_log.txt')


menu = [
    {'nome': 'Marketplaces',
     'rota': '/marketplaces'},
    {'nome': 'Produtos',
     'rota': '/produtos'},
    {'nome': 'Log de uso',
     'rota': '/historico'}
]