import json

def save_historic(linha: str, caminho_arquivo: str):
  arquivo = open(caminho_arquivo, 'a')
  arquivo.write(f'{linha}\n')
  arquivo.close()
