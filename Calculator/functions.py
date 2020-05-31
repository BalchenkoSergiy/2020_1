from Calculator import calsses

entry_list = []
#symbol = ''


def show_inserted(lable, symb, my_list):
    if symb != '+' and symb != '-' and symb != '/' and symb != '*' and len(my_list) <= 1:
        lable['text'] = f'{create_first_number(my_list, symb)}'
    elif symb == '+' or symb == '-' or symb == '/' or symb == '*':
        if len(entry_list) == 1:
            lable['text'] = f'{entry_list[0]} {create_symb(my_list, symb)}'
        else:
            lable['text'] = f'{entry_list[0]} {create_symb(my_list, symb)} {entry_list[2]}'
    elif len(my_list) > 1:
        lable['text'] = f'{entry_list[0]} {entry_list[1]} {create_second_number(my_list, symb)}'


def create_first_number(my_list, symb):
    if len(my_list) == 0:
        my_list.append(symb)
    elif len(my_list) > 0:
        my_list[0] = my_list[0] + symb
    return my_list[0]


def create_second_number(my_list, symb):
    if len(my_list) == 2:
        my_list.append(symb)
    elif len(my_list) > 2:
        my_list[2] = my_list[2] + symb
    return my_list[2]


def create_symb(my_list, symb):
    global symbol
    symbol = symb
    if len(my_list) == 1:
        my_list.append(symb)
    else:
        my_list[1] = symb
    return my_list[1]

def make_object(label, my_list):
    if len(my_list) == 3:
        result = calsses.Calc(my_list)
        if my_list[1] == '+':
            label['text'] = f'{result.plus()}'
            return result
        elif my_list[1] == '-':
            label['text'] = f'{result.minus()}'
            return result
        elif my_list[1] == '/':
            if check_zero(label, my_list) != 0:
                label['text'] = f'{result.divided()}'
                return result


        elif my_list[1] == '*':
            label['text'] = f'{result.multiply()}'
            return result

def check_zero(label, my_list):
    if my_list[1] == '/' and my_list[2] == '0':
        label['text'] = 'Must be not ZERO!'
        return 0
    return my_list

def clear_all(label, my_list):
    label['text'] = ''
    my_list.clear()
