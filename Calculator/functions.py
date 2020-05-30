entry_list = []
symbol = ''


def show_inserted(lable, symb, my_list):
    if symb != '+' and symb != '-' and symb != '/' and symb != '*':
        lable['text'] = f'{create_first_number(my_list, symb)}'
    elif symb != '+' and symb != '-' and symb != '/' and symb != '*' and len(my_list) == 2:
        lable['text'] = f'{create_second_number(my_list, symb)}'
    print(my_list)
    print(symbol)


def create_first_number(my_list, symb):
    #if len(my_list) > 0:
    my_list.append(symb)
    return my_list


def create_second_number(my_list, symb):
    global symbol
    symbol = symb



