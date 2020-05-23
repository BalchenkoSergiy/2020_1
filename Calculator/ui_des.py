from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('180x205+1000+300')
root['bg'] = 'grey'


# Створюю фрейм one
frame_one = Frame(root, bg='grey')
frame_one.pack()


# Ввід тексту
e_first_num = Entry(frame_one, bd=5)
e_first_num.pack(side='left', anchor='nw', ipadx=14, ipady=8, padx=4, pady=4)


# Створюю фрейм two
frame_two = Frame(root, bg='grey')
frame_two.pack()

# Створюю кнопки 7, 8, 9, +
my_button_c = Button(frame_two, text='7', bg='green', command=None)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_two, text='8', bg='green', command=None)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_two, text='9', bg='green', command=None)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_plus = Button(frame_two, text='+', bg='green', command=lambda: None)
my_button_plus.pack(side=LEFT, anchor='nw', ipadx=9, padx=2, pady=2)


# Створюю фрейм three
frame_three = Frame(root, bg='grey')
frame_three.pack()

# Створюю кнопки 4, 5, 6, -
my_button_c = Button(frame_three, text='4', bg='green', command=None)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_three, text='5', bg='green', command=None)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_three, text='6', bg='green', command=None)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_minus = Button(frame_three, text='-', bg='green', command=lambda: None)
my_button_minus.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)


# Створюю фрейм fore
frame_fore = Frame(root, bg='grey')
frame_fore.pack()

# Створюю кнопки 1, 2, 3, *
my_button_c = Button(frame_fore, text='1', bg='green', command=None)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_fore, text='2', bg='green', command=None)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_fore, text='3', bg='green', command=None)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_multiply = Button(frame_fore, text='*', bg='green', command=lambda: None)
my_button_multiply.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)


# Створюю фрейм five
frame_five = Frame(root, bg='grey')
frame_five.pack()

# Створюю кнопки 0, ',', C, /
my_button_c = Button(frame_five, text='0', bg='green', command=None)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)

my_button_c = Button(frame_five, text=',', bg='green', command=None)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=11, padx=2, pady=2)

my_button_c = Button(frame_five, text='C', bg='green', command=None)
my_button_c.pack(side=LEFT, anchor='nw', ipadx=9, padx=2, pady=2)

my_button_divide = Button(frame_five, text='/', bg='green', command=lambda: None)
my_button_divide.pack(side=LEFT, anchor='nw', ipadx=10, padx=2, pady=2)


# Створюю фрейм six
frame_six = Frame(root, bg='grey')
frame_six.pack()

# Створюю кнопку =
my_button = Button(frame_six, width=21, text='=', bg='red', command=None)
my_button.pack(padx=2, pady=2)


root.mainloop()