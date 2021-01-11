from ...utils.utils import save_in_archive, read_archive


def read() -> list:
    marketplaces = read_archive('logs/marketplaces.txt')
    return marketplaces


def write(name: str, description: str) -> None:
    line_formated = f'{name}; {description}'
    save_in_archive(line_formated, 'logs/marketplaces.txt')
