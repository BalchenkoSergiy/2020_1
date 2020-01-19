from GVKG.list_for_GVKG import *
from GVKG.func_for_list_GVKG import  *

first_result = pars_list(state_list)

#
users = list_users(user_list)
#
for i in first_result:
    print(i)

print('****************************************************************************************************************')
flag = 0
for i in users:
    flag += 1
    print(flag, '-->', i)

print('****************************************************************************************************************')

flag = 0
res_roles_list = find_user(users, first_result)
for i in res_roles_list:
    flag += 1
    print(f'{flag}--> ФІО: {i[2]}, Відділення: {i[0]} Посада: {i[1]}')

print('****************************************************************************************************************')
