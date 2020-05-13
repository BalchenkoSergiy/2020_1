from tkinter import *

root = Tk()
root.geometry('650x200+1000+300')

# Створюю фрейм one
frame_one = Frame(root)
frame_one.pack()


# Лейбл та ввід першої цифри
l_first_num = Label(frame_one, text='First number:')
l_first_num.pack(side='left', anchor='nw', ipadx=10)

e_first_num = Entry(frame_one, bd=5)
e_first_num.pack(side='left', anchor='nw')

# Створюю кнопки
my_button = Button(frame_one, text='+')
my_button.pack(side=LEFT, anchor='nw', ipadx=4, padx=6)

my_button = Button(frame_one, text='-')
my_button.pack(side=LEFT, anchor='nw', ipadx=5, padx=6)

my_button = Button(frame_one, text='*')
my_button.pack(side=LEFT, anchor='nw', ipadx=5, padx=6)

my_button = Button(frame_one, text='/')
my_button.pack(side=LEFT, anchor='nw', ipadx=5, padx=6)


# Лейбл та ввід другої цифри
l_sec_num = Label(frame_one, text='Second number:')
l_sec_num.pack(side='left', anchor='nw', padx=10)

e_sec_num = Entry(frame_one, bd=5)
e_sec_num.pack(side='left', anchor='ne')


# Створюю фрейм two
frame_two = Frame(root)
frame_two.pack()


# Створюю кнопку =
my_button = Button(frame_two, height=2, width=50, text='=')
my_button.pack(pady=20)


# Створюю фрейм three
frame_three = Frame(root)
frame_three.pack()


# Створюю кнопку =
l_result = Label(frame_three, height=2, width=50, text='This place for result')
l_result.pack(pady=10)





root.mainloop()



# entry_var_2 = Entry(root, bd=5)
# entry_var_2.insert(0, 'Hello')
# entry_var_2.insert(END, ' world')
# entry_var_2.delete(2, 6)
# entry_var_2.pack()

# entry_var_3 = Entry(root, bd=5)
# entry_var_3.insert(0, 'Hello')
# entry_var_3.insert(END, ' world')
# var_res = entry_var_3.get()
# entry_var_3.pack()

# print(var_res)

