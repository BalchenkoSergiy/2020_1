from tkinter import *
from tk_test_entry import classes

root = Tk()
root.geometry('650x200+1000+300')
root['bg'] = 'grey'
# Створюю фрейм one
frame_one = Frame(root, bg='grey')
frame_one.pack()

total_result = None

# Створюю функцію яка буде брати значення введених чисел і передавати їх у клас
def get_first():
    global total_result
    total_result = classes.Calc(e_first_num.get(), e_sec_num.get())
    l_result['text'] = f'First number: {e_first_num.get()}; Second number: {e_sec_num.get()};'




# Лейбл та ввід першої цифри
l_first_num = Label(frame_one, text='First number:', bg='grey')
l_first_num.pack(side='left', anchor='nw', ipadx=10)

e_first_num = Entry(frame_one, bd=5)
e_first_num.pack(side='left', anchor='nw')

# Створюю кнопки
my_button = Button(frame_one, text='+', bg='green')
my_button.pack(side=LEFT, anchor='nw', ipadx=4, padx=6)

my_button = Button(frame_one, text='-', bg='green')
my_button.pack(side=LEFT, anchor='nw', ipadx=5, padx=6)

my_button = Button(frame_one, text='*', bg='green')
my_button.pack(side=LEFT, anchor='nw', ipadx=5, padx=6)

my_button = Button(frame_one, text='/', bg='green')
my_button.pack(side=LEFT, anchor='nw', ipadx=5, padx=6)


# Лейбл та ввід другої цифри
l_sec_num = Label(frame_one, text='Second number:', bg='grey')
l_sec_num.pack(side='left', anchor='nw', padx=10)

e_sec_num = Entry(frame_one, bd=5)
e_sec_num.pack(side='left', anchor='ne')


# Створюю фрейм two
frame_two = Frame(root, bg='grey')
frame_two.pack()


# Створюю кнопку =
my_button = Button(frame_two, height=2, width=50, text='=', bg='red', command=get_first)
my_button.pack(pady=20)


# Створюю фрейм three
frame_three = Frame(root, bg='grey')
frame_three.pack()


# Створюю кнопку =
l_result = Label(frame_three, height=2, width=50, text='This place for result', bg='grey')
l_result.pack(pady=10)


root.mainloop()
