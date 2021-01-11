from ...utils.utils import save_in_archive, read_archive

def read() -> list:
    categories = read_archive('logs/categories.txt')
    return categories

def write(name: str, description: str) -> None:
    line_formated = f'{name}; {description}'
    save_in_archive(line_formated, 'logs/categories.txt')
