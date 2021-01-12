from datetime import datetime


def save_in_archive(new_line: str, path_file: str) -> None:
    file = open(path_file, 'a')
    file.write(f'{new_line}\n')
    file.close()


def read_archive(path: str) -> list:
    list_objs: list = []
    archive = open(path, 'r')

    for obj in archive:
        line_cleaned = obj.strip()  # clear caracteres and clear white spaces (\n \t \r ' ')
        data_line = line_cleaned.split(';')
        list_objs.append(data_line)

    archive.close()
    return list_objs


def save_logfile(log_name: str) -> None:
    """
    Saves system logs
    :param log_name:
    :return: None
    """
    current_datetime = datetime.now()
    current_formated_datetime = current_datetime.strftime('%d/%m/%Y %H:%M:%S')
    log_line = f'{current_formated_datetime} - {log_name}'
    save_in_archive(log_line, 'logs/logfile.txt')


def read_logfile():
    logs: list = []
    archive = open('logs/logfile.txt', 'r')

    for obj in archive:
        line_cleaned = obj.strip()  # clear caracteres and clear white spaces (\n \t \r ' ')
        data_line = line_cleaned.split('-')
        formated_line = {"date": data_line[0], "type": data_line[1], "where": data_line[2]}
        logs.append(formated_line)

    archive.close()
    return logs
