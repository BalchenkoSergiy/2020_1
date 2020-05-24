entry_list = []

def show_inserted(lable, symb, my_list):
    lable['text'] = f'{create_str(my_list, symb)}'

def create_str(my_list, symb):
    if len(my_list) > 0:
        my_list[0] = my_list[0] + symb
    elif len(my_list) == 0:
        my_list.append(symb)
    return my_list[0]
