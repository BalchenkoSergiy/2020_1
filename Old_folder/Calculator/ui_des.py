from tkinter import *
from Old_folder.Calculator.functions import *


root = Tk()
root.title('Calculator')
root.geometry('180x195+2800+300')
root['bg'] = 'grey'


# Створюю фрейм one
frame_one = Frame(root, bg='white')
frame_one.pack(fill='x')


# Ввід тексту
l_first_num = Label(frame_one, bd=5)
l_first_num.pack(anchor='nw',  ipady=4, padx=4, pady=4, fill='x')


# Створюю фрейм two
frame_two = Frame(root, bg='grey')
frame_two.pack()

# Створюю кнопку 7
my_button_c = Button(frame_two,
                     text='7',
                     bg='white',
                     activebackground='green',
                     command=lambda: create_object(l_first_num, '7'))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

# Створюю кнопку 8
my_button_c = Button(frame_two,
                     text='8',
                     bg='white',
                     activebackground='green',
                     command=lambda: create_object(l_first_num, '8'))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

# Створюю кнопку 9
my_button_c = Button(frame_two,
                     text='9',
                     bg='white',
                     activebackground='green',
                     command=lambda: create_object(l_first_num, '9'))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_plus = Button(frame_two,
                        text='+',
                        bg='white',
                        activebackground='green',
                        command=lambda: create_object(l_first_num, '+'))
my_button_plus.pack(side=LEFT, anchor='nw', ipadx=9, padx=2, pady=2)


# Створюю фрейм three
frame_three = Frame(root, bg='grey')
frame_three.pack()

# Створюю кнопку 4
my_button_c = Button(frame_three,
                     text='4',
                     bg='white',
                     activebackground='green',
                     command=lambda: create_object(l_first_num, '4'))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

# Створюю кнопку 5
my_button_c = Button(frame_three,
                     text='5',
                     bg='white',
                     activebackground='green',
                     command=lambda: create_object(l_first_num, '5'))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

# Створюю кнопку 6
my_button_c = Button(frame_three,
                     text='6',
                     bg='white',
                     activebackground='green',
                     command=lambda: create_object(l_first_num, '6'))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

# Створюю кнопку -
my_button_minus = Button(frame_three,
                         text='-',
                         bg='white',
                         activebackground='green',
                         command=lambda: create_object(l_first_num, '-'))
my_button_minus.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)


# Створюю фрейм fore
frame_fore = Frame(root, bg='grey')
frame_fore.pack()

# Створюю кнопку 1
my_button_c = Button(frame_fore,
                     text='1',
                     bg='white',
                     activebackground='green',
                     command=lambda: create_object(l_first_num, '1'))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

# Створюю кнопку 2
my_button_c = Button(frame_fore,
                     text='2',
                     bg='white',
                     activebackground='green',
                     command=lambda: create_object(l_first_num, '2'))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

# Створюю кнопку 3
my_button_c = Button(frame_fore,
                     text='3',
                     bg='white',
                     activebackground='green',
                     command=lambda: create_object(l_first_num, '3'))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

# Створюю кнопку *
my_button_multiply = Button(frame_fore,
                            text='*',
                            bg='white',
                            activebackground='green',
                            command=lambda: create_object(l_first_num, '*'))
my_button_multiply.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)


# Створюю фрейм five
frame_five = Frame(root, bg='grey')
frame_five.pack()

# Створюю кнопку 0
my_button_c = Button(frame_five,
                     text='0',
                     bg='white',
                     activebackground='green',
                     command=lambda: create_object(l_first_num, '0'))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

# Створюю кнопку ','
my_button_c = Button(frame_five,
                     text=',',
                     bg='white',
                     activebackground='green',
                     command=lambda: create_object(l_first_num, '.'))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=11, padx=2, pady=2)

# Створюю кнопку C
my_button_c = Button(frame_five,
                     text='C',
                     bg='white',
                     activebackground='green',
                     command=lambda: create_object(l_first_num, 'C'))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

# Створюю кнопку /
my_button_divide = Button(frame_five,
                          text='/',
                          bg='white',
                          activebackground='green',
                          command=lambda: create_object(l_first_num, '/'))
my_button_divide.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)


# Створюю фрейм six
frame_six = Frame(root, bg='grey')
frame_six.pack()

# Створюю кнопку =
my_button = Button(frame_six,
                   width=21,
                   text='=',
                   bg='red',
                   activebackground='green',
                   command=lambda: create_object(l_first_num, '='))
my_button.pack(padx=2, pady=2)


root.mainloop()