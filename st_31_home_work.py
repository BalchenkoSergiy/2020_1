import set_file


def main_print(path):
    tab = '\t'
    for pathes in path:
        if type(pathes[0]) == str:
            print(f'Folder: "{pathes[0]}"')
            if len(pathes) == 3:
                for i in pathes[1]:
                    print(f'{tab} --> {i}')
                for i in pathes[2]:
                    print(f'{tab} --> {i}')
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


# Start
hello = input('Привет, ты хочешь посмотреть что находится в какой-то папке? "YES"|"NO":')
if hello == "NO":
    print('ok')
elif hello == "YES":
    print('Хорошо!')
    my_path = input('Укажи путь к файлу:')
    my_main_path_list = set_file.main_all(my_path)  # List pathes
    #print(my_main_path_list)
    my_path_dict = set_file.create_dicts(my_path)
    #print(my_main_path_list)
    my_path_address = set_file.parse_path(my_path)
    print(f'Ты ввел: {my_path}')
    print('Держи дружище!')
    # Переформатирую каждый путь к файлу в список строк
    for i in my_main_path_list:
        i[0] = set_file.parse_path(i[0])


    # Вывожу корневую заданую папку
    main_folder = my_path_address[-1]

    # Укорачиваю первый путь в общем списке
    for i in my_main_path_list:
        if my_main_path_list[0][0][-1] == main_folder:
            my_main_path_list[0][0] = main_folder

    # Узнаю индекс названия заданой корневой папки (он постоянный в каждом пути)
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

    main_print(my_main_path_list)
else:
    print('Have a nice day!')