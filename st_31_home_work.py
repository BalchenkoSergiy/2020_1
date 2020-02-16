import os
test = os.listdir()
# ['.git', '.gitignore', '.idea', 'DocumentTemplate', 'GVKG', 'html_files_for_templates',
# 'procedures_for_teach', 'st_18_home_work.py', 'st_21_home_work.py', 'st_24_home_work.py',
# 'st_26_home_work.py', 'st_28_home_work.py', 'st_31_home_work.py', 'st_datetime_module.py',
# 'st_dictionaries.py', 'st_for_while.py', 'st_functions.py', 'st_functions_part_2.py',
# 'st_functions_part_3.py', 'st_game_for_liza.py', 'st_if.py', 'st_lists.py', 'st_modules.py',
# 'st_modules_2_libs.py', 'st_mut_and_unmut_objects.py', 'st_notes.py', 'st_sets_and_frozensets.py',
# 'st_strings.py', 'st_TARGET_part_1.py', 'st_TARGET_part_2.py', 'st_tuples.py', 'test_folder_for_check',
# 't_sql_certification', 'venv', '__pycache__']


test = os.getcwd()
# C:\Users\sergi\PycharmProjects\st_course_1


test = os.chdir('test_folder_for_check')
test = os.getcwd()
# C:\Users\sergi\PycharmProjects\st_course_1\test_folder_for_check

test = os.listdir()
# ['folder_A', 'folder_B', 'folder_C']

test = os.chdir('..')
test = os.getcwd()
# C:\Users\sergi\PycharmProjects\st_course_1


for i in os.walk(r'C:\Users\sergi\PycharmProjects\st_course_1\test_folder_for_check'):
    print(i)
#print(test)


def main_all(path):
    data_list = []
    for i in os.walk(path):
        data_list.append(list(i))
    return data_list


def main_folder(path):
    data_list = main_all(path)[0][1]
    return data_list

print('**************************************************************************************************************')
test_main_list = main_all(r'C:\Users\sergi\PycharmProjects\st_course_1\test_folder_for_check')
print(test_main_list)

test_list = main_folder(r'C:\Users\sergi\PycharmProjects\st_course_1\test_folder_for_check')
print('result -->:', test_list)

new_path = str(test_main_list[0][0] + '\\' + test_list[0])
print(new_path)

if new_path in test_main_list[1]:
    print('ok')
else:
    print('no find')

count = 0
for i in test_list:
    print(f'{i}:')
    for a in test_main_list[1:]:
        if a[-3][-8:] == i:
            print(f'\t{a[-2]}')
        elif a[-3][-19:-11] == i:
            print(f'\t\t{a[-1]}')

#print('--------->', test_main_list[1][-3][-8:])

        #if i[-1] == []:
        #    print(f'\t{i[-2][count]}:')
        #else:
        #    print(f'\t \t{i[-1]}')



