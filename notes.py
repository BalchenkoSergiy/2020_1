from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')

# -----------------------------------------------------------------------------------------------------
# frame_top = LabelFrame(root, text="Using grid", padx=10, pady=10)
# frame_top.grid(column=0, row=1)
#
# button_one = Button(frame_top, text='1', font='15', fg='#fff', bg='#3498db', width=8, height=4)
# button_one.grid(column=0, row=1)
#
# button_two = Button(frame_top, text='2', font='15', fg='#fff', bg='#2ecc71', width=8, height=4)
# button_two.grid(column=1, row=1)
#
# button_onetwo = Button(frame_top, text='3', font='15', fg='#fff', bg='#3498db', width=8, height=4)
# button_onetwo.grid(column=2, row=1)
#
# button_twoone = Button(frame_top, text='4', font='15', fg='#fff', bg='#2ecc71', width=8, height=4)
# button_twoone.grid(column=0, row=2)
#
# button_twotwo = Button(frame_top, text='5', font='15', fg='#fff', bg='#3498db', width=8, height=4)
# button_twotwo.grid(column=1, row=2)
#
# button_two_one = Button(frame_top, text='6', font='15', fg='#fff', bg='#2ecc71', width=8, height=4)
# button_two_one.grid(column=2, row=2)
#
#
# frame_bottom = LabelFrame(root, text="frame_bottom", padx=10, pady=10)
# frame_bottom.grid(column=1, row=1, padx=20)
#
# label_THREE = Label(frame_bottom, text='THREE', font='15', fg='#fff', bg='#f1c40f', width=8, height=4)
# label_THREE.pack(side=LEFT)
#
# label_FOUR = Label(frame_bottom, text='FOUR', font='15', fg='#fff', bg='#34495e', width=8, height=4)
# label_FOUR.pack(side=LEFT)

# f_top = LabelFrame(root, text="Top Frame", padx=10, pady=10)
# f_top.pack(pady=10)

# f_bottom = LabelFrame(root, text="Bottom Frame", padx=10, pady=10)
# f_bottom.pack()

# label_one     = Label(f_top, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(side=LEFT)
# label_two     = Label(f_top, text="2", font="15", fg="#fff", bg="#2ecc71", width=8, height=4).pack(side=LEFT)
# label_three   = Label(f_bottom, text="3", font="15", fg="#fff", bg="#f1c40f", width=8, height=4).pack(side=LEFT)
# label_four    = Label(f_bottom, text="4", font="15", fg="#fff", bg="#34495e", width=8, height=4).pack(side=LEFT)

# label_one = Label(root, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(expand=1, anchor=NE)
# -----------------------------------------------------------------------------------------------------

# f = Frame(root)
# f.pack(pady=10)
#
# btn_list = [
#     '7', '8', '9',
#     '4', '5', '6',
#     '1', '2', '3',
#     '0']
#
# row = 0
# column = 0
#
# for i in btn_list:
#     if i == '0':
#         Button(f, text=i, padx=10, pady=5).grid(row=row, columnspan=3)
#     else:
#         Button(f, text=i, padx=10, pady=5).grid(row=row, column=column)
#     column += 1
#     if column == 3:
#         column = 0
#         row += 1
# Форма реєстрації -----------------------------------------------------------------------------
#l_user = Label(root, text="Login:").grid(row=0, column=0, padx=10, pady=10, sticky=W)
#e_user = Entry(root).grid(row=0, column=1, columnspan=2, padx=10, sticky=W+E)
#
#l_pass = Label(root, text="Password:").grid(row=1, column=0, padx=10, sticky=W)
#e_pass = Entry(root, show='*').grid(row=1, column=1, columnspan=2, padx=10, sticky=W+E)
#
#btn_login = Button(root, text="Вхід", padx=5).grid(row=2, column=0, padx=10, pady=10, sticky=W)
#btn_reg = Button(root, text="Реєистрація", padx=5).grid(row=2, column=1)
#btn_forgot = Button(root, text="Забули пароль?", padx=5).grid(row=2, column=2, padx=10)

#Метод place()
#from tkinter import *
#
#root = Tk()
#root.geometry('400x400+1000+300')


# l1 = Label(root, text="Hello world!", bg="#3498db", fg="#fff", font="16", padx=20, pady=8)
# l1.place(x=0, y=0)
#
# l2 = Label(root, text="Hello world!", bg="#2ecc71", fg="#fff", font="16", padx=20, pady=8)
# l2.place(relx=0.5, rely=0.5, anchor='c')

# btn1 = Button(text='Button 1', bg="#3498db", fg="#fff", font="16", padx=20, pady=8)
# btn1.place(x=0, y=0)
#
# btn2 = Button(text='Button 1', bg="#2ecc71", fg="#fff", font="16", padx=20, pady=8)
# btn2.place(relx=0.5, rely=0.5, anchor='c')
#
# btn3 = Button(text='Button 1', bg="#f1c40f", fg="#fff", font="16", padx=20, pady=8)
# btn3.place(relx=1, rely=1, anchor='se')

l = Label(root, bg="#000")
l.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

btn2 = Button(text='Button 1', bg="#2ecc71", fg="#fff", font="16", padx=20, pady=8)
btn2.place(relx=0.5, rely=0.5, anchor='c')

root.mainloop()