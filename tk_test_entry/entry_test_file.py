from tkinter import *
from tk_test_entry import classes

root = Tk()
root.title('My easy calc')
root.geometry('650x200+1000+300')
root['bg'] = 'grey'

result = 0
total_result = None
param = None
opt = ''
my_list = [opt, 'first', 'second']

# Створюю функцію яка буде брати значення введених чисел і передавати їх у клас
def logic(option):
    global result
    global opt
    try:
        first_number = int(e_first_num.get())
    except:
        pass
    try:
        second_number = int(e_sec_num.get())
    except:
        pass
    total_result = classes.Calc(first_number, second_number)
    if option == '+':
        opt = '+'
        l_result['text'] = f'{e_first_num.get()} {option} {e_sec_num.get()}'
        # checking_insert('+')
        result = total_result.plus()
    if option == '-':
        opt = '-'
        l_result['text'] = f'{e_first_num.get()} {option} {e_sec_num.get()}'
        result = total_result.minus()
    if option == '/':
        opt = '/'
        l_result['text'] = f'{e_first_num.get()} {option} {e_sec_num.get()}'
        result = total_result.divided()
    if option == '*':
        opt = '*'
        l_result['text'] = f'{e_first_num.get()} {option} {e_sec_num.get()}'
        result = total_result.multiply()
    result = [opt, result, e_first_num.get(), e_sec_num.get()]


def checking_insert(option):
    if option == '+' or '-' or '*' or '/':
        if type(e_first_num.get()) != int or type(e_sec_num.get()) != int:
            l_result['text'] = 'Please insert only integer number'


def result_total():
    l_result['text'] = f'{result[2]} {result[0]} {result[3]} = {result[1]};'


def del_all():
    e_first_num.delete(0, END)
    e_sec_num.delete(0, END)
    l_result['text'] = 'Insert your numbers please'


# Створюю фрейм one
frame_one = Frame(root, bg='grey')
frame_one.pack()



# Лейбл та ввід першої цифри
l_first_num = Label(frame_one, text='First number:', bg='grey')
l_first_num.pack(side='left', anchor='nw', ipadx=10)

e_first_num = Entry(frame_one, bd=5)
e_first_num.pack(side='left', anchor='nw')

# Створюю кнопки
my_button_c = Button(frame_one, text='C', bg='green', command=del_all)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=5, padx=2)

my_button_plus = Button(frame_one, text='+', bg='green', command=lambda: logic('+'))
my_button_plus.pack(side=LEFT, anchor='nw', ipadx=5, padx=2)

my_button_minus = Button(frame_one, text='-', bg='green', command=lambda: logic('-'))
my_button_minus.pack(side=LEFT, anchor='nw', ipadx=5, padx=2)

my_button_multiply = Button(frame_one, text='*', bg='green', command=lambda: logic('*'))
my_button_multiply.pack(side=LEFT, anchor='nw', ipadx=5, padx=2)

my_button_divide = Button(frame_one, text='/', bg='green', command=lambda: logic('/'))
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
my_button = Button(frame_two, height=2, width=50, text='=', bg='red', command=result_total)
my_button.pack(pady=20)

# Створюю фрейм three
frame_three = Frame(root, bg='grey')
frame_three.pack()

# Створюю лейбл текст для відображенню результата
l_result = Label(frame_three, height=2, width=50, text='This place for result', bg='grey')
l_result.pack(pady=10)

root.mainloop()
