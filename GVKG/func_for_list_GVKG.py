from GVKG.list_for_GVKG import *
import re

def replace_string (var):
    ir3 = ''
    if var[0] in [' ', '\t'] and var[-1] in [' ', '\t']:
        ir3 = var[1:-1]
    elif var[0] in [' ', '\t']:
        ir3 = var[1:]
    elif var[-1] in [' ', '\t']:
        ir3 = var[:-1]
    else: ir3 = var
    return ir3

def del_space(var):
    ind = var.index(' ')
    res = var[:ind]
    return res



def pars_list (list_var):
    new_list = []
    for i in list_var:
        var = [re.sub(r'\s+', ' ', replace_string(i[0])), re.sub(r'\s+', ' ', replace_string(i[1])), re.sub(r'\s+', ' ', replace_string(i[2]))]
        new_list.append(var)
    return new_list


def list_users (start_list):
    result_list = []
    for i in start_list:
        result_list.append(replace_string (i))
    return result_list


def find_user(var_users, var_roles):
    result = []

    for i in var_users:
        for s in var_roles:
            if s[2].find(del_space(i)) != -1:
                result.append(s)
            else:
                continue
    return result





#ir3 = i2[1:-1]
#print(ir3)

#ir4 = ''.join(ir3)
#print(ir4)


