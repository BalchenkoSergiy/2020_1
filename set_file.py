import os

def set_path(path):
    return os.chdir(path)


def main_all(path):
    data_list = []
    for i in os.walk(path):
        data_list.append(list(i))
    return data_list


def main_folder(path):
    data_list = main_all(path)[0][1]
    return data_list


def parse_path(path): # парсим адресною строку на путь.
    path_str = str(path)
    result = path_str.split('\\')
    return result


def create_dicts(path):
    result_one = main_all(path)
    result_dict = {}
    for lists in result_one:
        result_dict[lists[0]] = lists[1:]
    return result_dict