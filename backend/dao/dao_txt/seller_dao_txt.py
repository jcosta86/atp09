from ...utils.utils import save_in_archive, read_archive


def read() -> list:
    sellers = read_archive('logs/sellers.txt')
    return sellers


def write(fullname: str, email: str, phone: str) -> None:
    line_formated = f'{fullname}; {email}; {phone}'
    save_in_archive(line_formated, 'logs/sellers.txt')
