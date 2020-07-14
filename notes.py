from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')

label_one = Label(root, text='TOP', font='15', fg='#fff', bg='#3498db', width=8, height=4)
label_one.pack(side=TOP)

label_one = Label(root, text='BOTTOM', font='15', fg='#fff', bg='#3498db', width=8, height=4)
label_one.pack(side=BOTTOM)

label_one = Label(root, text='LEFT', font='15', fg='#fff', bg='#3498db', width=8, height=4)
label_one.pack(side=LEFT)

label_one = Label(root, text='RIGHT', font='15', fg='#fff', bg='#3498db', width=8, height=4)
label_one.pack(side=RIGHT)

#f_top = Frame(root)
#f_top.pack()

#f_bottom = Frame(root)
#f_bottom.pack()

#f_top = LabelFrame(root, text="Top Frame", padx=10, pady=10)
#f_top.pack(pady=10)

#f_bottom = LabelFrame(root, text="Bottom Frame", padx=10, pady=10)
#f_bottom.pack()

#label_one     = Label(f_top, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(side=LEFT)
#label_two     = Label(f_top, text="2", font="15", fg="#fff", bg="#2ecc71", width=8, height=4).pack(side=LEFT)
#label_three   = Label(f_bottom, text="3", font="15", fg="#fff", bg="#f1c40f", width=8, height=4).pack(side=LEFT)
#label_four    = Label(f_bottom, text="4", font="15", fg="#fff", bg="#34495e", width=8, height=4).pack(side=LEFT)

#label_one = Label(root, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(expand=1, anchor=NE)

root.mainloop()