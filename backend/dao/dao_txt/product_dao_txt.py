from ...utils.utils import save_in_archive, read_archive


def read() -> list:
    products = read_archive('logs/products.txt')
    return products


def write(name: str, description: str, price: float) -> None:
    line_formated = f'{name}; {description}; {price}'
    save_in_archive(line_formated, 'logs/products.txt')
