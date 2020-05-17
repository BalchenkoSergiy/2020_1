from tkinter import *
from tk_test_entry import classes

root = Tk()
root.title('My easy calc')
root.geometry('650x200+1000+300')
root['bg'] = 'grey'


# Створюю функцію яка буде брати значення введених чисел і передавати їх у клас
def logic():
    global total_result
    total_result = classes.Calc(e_first_num.get(), e_sec_num.get())
    if param == '+':
        result = total_result.plus()
    if param == '-':
        result = total_result.minus()
    if param == '/':
        result = total_result.divided()
    if param == '*':
        result = total_result.multiply()
    l_result['text'] = f'{e_first_num.get()} {param} {e_sec_num.get()} = {result};'


# Створюю функцію яка встановлює параметр знаку дії
def set_plus():
    global param
    param = '+'


# Створюю функцію яка встановлює параметр знаку дії
def set_minus():
    global param
    param = '-'


# Створюю функцію яка встановлює параметр знаку дії
def set_divided():
    global param
    param = '/'


# Створюю функцію яка встановлює параметр знаку дії
def set_multiply():
    global param
    param = '*'


def del_all():
    e_first_num.delete(0, END)
    e_sec_num.delete(0, END)
    l_result['text'] = 'Insert your numbers please'

# Створюю фрейм one
frame_one = Frame(root, bg='grey')
frame_one.pack()

total_result = None
param = None


# Лейбл та ввід першої цифри
l_first_num = Label(frame_one, text='First number:', bg='grey')
l_first_num.pack(side='left', anchor='nw', ipadx=10)

e_first_num = Entry(frame_one, bd=5)
e_first_num.pack(side='left', anchor='nw')

# Створюю кнопки
my_button_c = Button(frame_one, text='C', bg='green', command=del_all)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=5, padx=2)

my_button_plus = Button(frame_one, text='+', bg='green', command=set_plus)
my_button_plus.pack(side=LEFT, anchor='nw', ipadx=5, padx=2)

my_button_minus = Button(frame_one, text='-', bg='green', command=set_minus)
my_button_minus.pack(side=LEFT, anchor='nw', ipadx=5, padx=2)

my_button_multiply = Button(frame_one, text='*', bg='green', command=set_multiply)
my_button_multiply.pack(side=LEFT, anchor='nw', ipadx=5, padx=2)

my_button_divide = Button(frame_one, text='/', bg='green', command=set_divided)
my_button_divide.pack(side=LEFT, anchor='nw', ipadx=5, padx=2)


# Лейбл та ввід другої цифри
l_sec_num = Label(frame_one, text='Second number:', bg='grey')
l_sec_num.pack(side='left', anchor='nw', padx=10)

e_sec_num = Entry(frame_one, bd=5)
e_sec_num.pack(side='left', anchor='ne')


# Створюю фрейм two
frame_two = Frame(root, bg='grey')
frame_two.pack()


# Створюю кнопку =
my_button = Button(frame_two, height=2, width=50, text='=', bg='red', command=logic)
my_button.pack(pady=20)


# Створюю фрейм three
frame_three = Frame(root, bg='grey')
frame_three.pack()


# Створюю кнопку =
l_result = Label(frame_three, height=2, width=50, text='This place for result', bg='grey')
l_result.pack(pady=10)



root.mainloop()
