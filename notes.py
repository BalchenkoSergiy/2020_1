from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')


frame_top = Frame(root)
frame_top.pack()

label_one = Label(frame_top, text='ONE', font='15', fg='#fff', bg='#3498db', width=8, height=4)
label_one.pack(side=LEFT)

label_one = Label(frame_top, text='TWO', font='15', fg='#fff', bg='#2ecc71', width=8, height=4)
label_one.pack(side=LEFT)


frame_bottom = Frame(root)
frame_bottom.pack()

label_one = Label(frame_bottom, text='THREE', font='15', fg='#fff', bg='#f1c40f', width=8, height=4)
label_one.pack(side=LEFT)

label_one = Label(frame_bottom, text='FOUR', font='15', fg='#fff', bg='#34495e', width=8, height=4)
label_one.pack(side=LEFT)





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