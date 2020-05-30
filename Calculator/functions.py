entry_list = []
symbol = ''


def show_inserted(lable, symb, my_list):
    global symbol
    if symb != '+' and symb != '-' and symb != '/' and symb != '*':
        lable['text'] = f'{create_str(my_list, symb)}'
    else:
        symbol = symb
    print(my_list)
    print(symbol)


def create_str(my_list, symb):
    global symbol
    if symbol == '':
        if len(my_list) > 0:
            my_list[0] = my_list[0] + symb
        elif len(my_list) == 0:
            my_list.append(symb)
        return my_list[0]
    else:
        if len(my_list) > 1:
            my_list[1] = my_list[1] + symb
        elif len(my_list) == 1:
            my_list.append(symb)
        return my_list[1]



