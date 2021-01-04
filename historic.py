def save_historic(new_line: str, path_file: str):
  file = open(path_file, 'a')
  file.write(f'{new_line}\n')
  file.close()
