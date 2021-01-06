

def save_in_database(new_line: str, path_file: str) -> None:
    """
  Saves system objects in database
  :param new_line:
  :param path_file:
  :return: None
  """
    file = open(path_file, 'a')
    file.write(f'{new_line}\n')
    file.close()


"""def show_database_marketplaces() -> list:
  lista_linhas_arquivo = []
  arquivo = open(caminho, 'r')
  for lista in arquivo:
    lista.strip() # retira caracteres de escape e espacos branco (\n \t \r ' ')
    lista.split(';') # transforma a string em uma lista de acordo com o caracter passado como argumento
    lista = f'{lista}'
    lista_linhas_arquivo.append(lista)
  arquivo.close()
  return lista_linhas_arquivo"""
