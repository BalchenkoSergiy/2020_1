import os
import zipfile

my_path =f'C:\\Users\\Professional\\PycharmProjects\\notes_for_study\\st_notes_less\\folder'

res = os.walk(my_path)
for i in res:
    print(f'1--> {i}')
tab = '    '

print('***************************************************************************')
res = os.path.abspath(my_path)
print(f'2--> {res}')
# C:\Users\Professional\PycharmProjects\notes_for_study\st_notes_less\folder

print('***************************************************************************')
res = os.path.basename(my_path)
print(f'3--> {res}')
# folder

print('***************************************************************************')
res = os.path.dirname(my_path)
print(f'4--> {res}')
# C:\Users\Professional\PycharmProjects\notes_for_study\st_notes_less

print('***************************************************************************')
res = os.path.exists(my_path)
print(f'5--> {res}')
# True

print('***************************************************************************')
res = os.path.expanduser(my_path)
print(f'6--> {res}')
# C:\Users\Professional\PycharmProjects\notes_for_study\st_notes_less\folder

print('***************************************************************************')
res = os.path.relpath(my_path)
print(f'7--> {res}')
# folder


print('***************************************************************************')
res = os.path.splitdrive(my_path)
print(f'8--> {res}')
# ('C:', '\\Users\\Professional\\PycharmProjects\\notes_for_study\\st_notes_less\\folder')

print('***************************************************************************')
res = os.walk(my_path)
for i in res:
    print(f'1 --> {os.path.relpath(i[0])}:')
    if i[1] != []:
        print(f'2 --> {tab}{i[1]}')
    print(f'3 --> {tab * 2}{i[2]}')

print('***************************************************************************')
# Зберігаю у змінну шлях до папки з майбутнім архівом:
folder_path = 'C:\\Users\\Professional\\PycharmProjects\\notes_for_study\\st_notes_less\\folder'

# Зберігаю у змінну шлях до архіву:
zip_path = 'C:\\Users\\Professional\\PycharmProjects\\notes_for_study\\st_notes_less\\folder\\my_zip.zip'

# Зберігаю із ім'ям архіву:
zip_name = 'my_zip.zip'

# Створюю архів по заданому адресу і з заданим ім'ям у режимі перезапису:
my_zip = zipfile.ZipFile(zip_path, 'w')

# Записую файл у архів використовуючи режим упаковки (рекомендується) compresslevel=zipfile.ZIP_DEFLATED.
# Я вказую другим параметром 'new.txt', для переіменування файлу 1.txt а також для того щоб не поміщати у архів
# весь шлях з диску "С"
my_zip.write('C:\\Users\\Professional\\PycharmProjects\\notes_for_study\\st_notes_less\\folder\\1.txt', 'new.txt',
             compresslevel=zipfile.ZIP_DEFLATED)

# Закриваю архів:
my_zip.close()

print('***************************************************************************')
# Запаковую у архів каталог із всім вмістом. (А не один файл)

# Зберігаю у змінну шлях до папки з майбутнім архівом:
folder_path = 'C:\\Users\\Professional\\PycharmProjects\\notes_for_study\\st_notes_less\\folder'

# Зберігаю у змінну шлях до архіву:
zip_path = 'C:\\Users\\Professional\\PycharmProjects\\notes_for_study\\st_notes_less\\folder\\my_zip_cat.zip'

# Зберігаю із ім'ям архіву:
zip_name = 'my_zip_cat.zip'

# Створюю архів по заданому адресу і з заданим ім'ям у режимі перезапису:
my_zip_cat = zipfile.ZipFile(zip_path, 'w')

# Циклом прохожусь по результату обробки папки модулем OS по адресу папки яку ми хочемо додати у архів.
# Оскільки ми маємо список кортежів із трьох складових ми розпаковуємо їх як: folder, subfolders, files
for folder, subfolders, files in os.walk(folder_path):
    # Створюю цикл у якому я рухаюсь лише по files:
    for file in files:
        # Оскільки наш архів знаходиться в середині папки яку я хочу помістити у нього, мені потрібно сам архів
        # проігнорувати і пройти мімо (попередній, тестовий архів також):
        if file == zip_name:
            continue
        if file == 'my_zip.zip':
            continue
        # За допомогою os.path.join я об'єдную в один адрес частинки із folder+files і записую у архів
        # А також, для того щоб у архів не попадав весь шлях із диску "С" я використовую метод
        # os.path.relpath який обрізає весь попередній шлях до папки (folder_path) який нам не потрібен
        my_zip_cat.write(os.path.join(folder, file),
        os.path.relpath(os.path.join(folder, file), folder_path),
        compresslevel=zipfile.ZIP_DEFLATED)



# Закриваю архів:
my_zip.close()