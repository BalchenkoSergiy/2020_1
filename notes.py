from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')


frame_top = LabelFrame(root, text="frame_top", padx=10, pady=10)
frame_top.grid()

button_one = Button(frame_top, text='1', font='15', fg='#fff', bg='#3498db', width=8, height=4)
button_one.grid(column=0, row=1)

button_two = Button(frame_top, text='2', font='15', fg='#fff', bg='#2ecc71', width=8, height=4)
button_two.grid(column=1, row=1)

button_onetwo = Button(frame_top, text='3', font='15', fg='#fff', bg='#3498db', width=8, height=4)
button_onetwo.grid(column=2, row=1)

button_twoone = Button(frame_top, text='4', font='15', fg='#fff', bg='#2ecc71', width=8, height=4)
button_twoone.grid(column=0, row=2)

button_twotwo = Button(frame_top, text='5', font='15', fg='#fff', bg='#3498db', width=8, height=4)
button_twotwo.grid(column=1, row=2)

button_two_one = Button(frame_top, text='6', font='15', fg='#fff', bg='#2ecc71', width=8, height=4)
button_two_one.grid(column=2, row=2)


frame_bottom = LabelFrame(root, text="frame_bottom", padx=10, pady=10)
frame_bottom.grid(pady=10)

label_THREE = Label(frame_bottom, text='THREE', font='15', fg='#fff', bg='#f1c40f', width=8, height=4)
label_THREE.pack(side=LEFT)

label_FOUR = Label(frame_bottom, text='FOUR', font='15', fg='#fff', bg='#34495e', width=8, height=4)
label_FOUR.pack(side=LEFT)





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