

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
