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

def main_print(path):
    tab = '\t'
    for pathes in path:
        if type(pathes[0]) == str:
            print(f'Folder: "{pathes[0]}"')
            if len(pathes) == 3:
                for i in pathes[1]:
                    print(f'{tab} {i}')
                for i in pathes[2]:
                    print(f'{tab} {i}')
            if len(pathes) == 2:
                pathes[0] = ' --> '.join(map(str, pathes[0]))
                print(f'Folder: {pathes[0]}')
                for i in pathes[1]:
                    print(f'{tab} -->: {i}')
        else:
            if len(pathes) == 3:
                for i in pathes[1]:
                    print(f'{tab} {i}')
                for i in pathes[2]:
                    print(f'{tab} {i}')
            if len(pathes) == 2:
                pathes[0] = ' --> '.join(map(str, pathes[0]))
                print(f'Folder: {pathes[0]}')
                for i in pathes[1]:
                    print(f'{tab} -->: {i}')


hello = input('Привет, ты хочешь посмотреть что находится в какой-то папке? "YES"|"NO":')
if hello == "NO":
    print('ok')
elif hello == "YES":
    print('Хорошо!')
    my_path = input('Укажи путь к файлу:')
    my_main_path_list = main_all(my_path)  # List pathes

    my_path_dict = create_dicts(my_path)

    my_path_address = parse_path(my_path)
    print(f'Ты ввел: {my_path}')
    print('Держи дружище!')
    # Переформатирую каждый путь к файлу в список строк
    for i in my_main_path_list:
        i[0] = parse_path(i[0])

    # Вывожу корневую заданую папку
    main_folder = my_path_address[-1]

    # Укорачиваю первый путь в общем списке
    for i in my_main_path_list:
        if my_main_path_list[0][0][-1] == main_folder:
            my_main_path_list[0][0] = main_folder

    # Узнаю индекс индекс названия заданой корневой папки (он постоянный в каждом пути)
    temp_var = []
    count = my_main_path_list[1][0].index(main_folder)

    # Укорачиваю отображение путей от корневой папки
    for i in my_main_path_list[1:]:
        i[0] = i[0][count:]

    # удаляю пустые списки
    for pathes in my_main_path_list:
        for lists in pathes:
            if lists == []:
                pathes.remove(lists)

    main_print(my_path)

else:
    pass