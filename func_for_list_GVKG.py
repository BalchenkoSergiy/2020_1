from list_for_GVKG import *

test_list = [' one ', ' two ', ' three ']
new_list = []
test_string = ' one '


def change_first_symbo(var):
    res_str = None
    temp_list = list(var)
    res_str = ''.join(temp_list)
    return res_str

res = change_first_symbo(test_string)
print(res)

