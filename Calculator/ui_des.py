from tkinter import *
from Calculator import functions

root = Tk()
root.title('Calculator')
root.geometry('180x195+1000+300')
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

# Створюю кнопки 7, 8, 9, +
my_button_c = Button(frame_two,
                     text='7',
                     bg='white',
                     activebackground='green',
                     command=lambda: functions.show_inserted(l_first_num, '7', functions.entry_list))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_two,
                     text='8',
                     bg='white',
                     activebackground='green',
                     command=lambda: functions.show_inserted(l_first_num, '8', functions.entry_list))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_two,
                     text='9',
                     bg='white',
                     activebackground='green',
                     command=lambda: functions.show_inserted(l_first_num, '9', functions.entry_list))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_plus = Button(frame_two,
                        text='+',
                        bg='white',
                        activebackground='green',
                        command=lambda: functions.show_inserted(l_first_num, '+', functions.entry_list))
my_button_plus.pack(side=LEFT, anchor='nw', ipadx=9, padx=2, pady=2)


# Створюю фрейм three
frame_three = Frame(root, bg='grey')
frame_three.pack()

# Створюю кнопки 4, 5, 6, -
my_button_c = Button(frame_three,
                     text='4',
                     bg='white',
                     activebackground='green',
                     command=lambda: functions.show_inserted(l_first_num, '4', functions.entry_list))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_three,
                     text='5',
                     bg='white',
                     activebackground='green',
                     command=lambda: functions.show_inserted(l_first_num, '5', functions.entry_list))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_three,
                     text='6',
                     bg='white',
                     activebackground='green',
                     command=lambda: functions.show_inserted(l_first_num, '6', functions.entry_list))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_minus = Button(frame_three,
                         text='-',
                         bg='white',
                         activebackground='green',
                         command=lambda: functions.show_inserted(l_first_num, '-', functions.entry_list))
my_button_minus.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)


# Створюю фрейм fore
frame_fore = Frame(root, bg='grey')
frame_fore.pack()

# Створюю кнопки 1, 2, 3, *
my_button_c = Button(frame_fore,
                     text='1',
                     bg='white',
                     activebackground='green',
                     command=lambda: functions.show_inserted(l_first_num, '1', functions.entry_list))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_fore,
                     text='2',
                     bg='white',
                     activebackground='green',
                     command=lambda: functions.show_inserted(l_first_num, '2', functions.entry_list))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_fore,
                     text='3',
                     bg='white',
                     activebackground='green',
                     command=lambda: functions.show_inserted(l_first_num, '3', functions.entry_list))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_multiply = Button(frame_fore,
                            text='*',
                            bg='white',
                            activebackground='green',
                            command=lambda: functions.show_inserted(l_first_num, '*', functions.entry_list))
my_button_multiply.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)


# Створюю фрейм five
frame_five = Frame(root, bg='grey')
frame_five.pack()

# Створюю кнопки 0, ',', C, /
my_button_c = Button(frame_five,
                     text='0',
                     bg='white',
                     activebackground='green',
                     command=lambda: functions.show_inserted(l_first_num, '0', functions.entry_list))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_five,
                     text=',',
                     bg='white',
                     activebackground='green',
                     command=lambda: functions.show_inserted(l_first_num, '.', functions.entry_list))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=11, padx=2, pady=2)

my_button_c = Button(frame_five,
                     text='C',
                     bg='white',
                     activebackground='green',
                     command=lambda: functions.clear_all(l_first_num, functions.entry_list))
my_button_c.pack(side=LEFT, anchor='nw', ipadx=9, padx=2, pady=2)

my_button_divide = Button(frame_five,
                          text='/',
                          bg='white',
                          activebackground='green',
                          command=lambda: functions.show_inserted(l_first_num, '/', functions.entry_list))
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
                   command=lambda: functions.make_object(l_first_num, functions.entry_list))
my_button.pack(padx=2, pady=2)


root.mainloop()