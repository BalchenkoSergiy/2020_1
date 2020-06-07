from tkinter import *

root = Tk()

'''
Створити програму, яка складається із семи кнопок, кольори кнопок відповідають кольорам веселки. 
При натисканні на кнопку у текстове поле повинен вставлятись код кольору, а в мітку - назва кольору.
#ff0000: Червоний
#ff7d00: Оранжевий
#ffff00: Жовтий
#00ff00: Зелений
#007dff: Голубий
#0000ff: Синій
#7d00ff: Фіолетовий
'''


def get_color(text_color, hex_color):
    l['text'] = text_color
    e.delete(0, END)
    e.insert(0, hex_color)


l = Label(root)
e = Entry(root, width=30, justify='center')
l.pack()
e.pack()

btn_red = Button(root, bg="#ff0000", command=lambda: get_color('Червоний', '#ff0000'))
btn_red.pack(fill=X)

btn_orange = Button(root, bg="#ff7d00", command=lambda: get_color('Оранжевий', '#ff7d00'))
btn_orange.pack(fill=X)

btn_yellow = Button(root, bg="#ffff00", command=lambda: get_color('Жовтий', '#ffff00'))
btn_yellow.pack(fill=X)

btn_green = Button(root, bg="#00ff00", command=lambda: get_color('Зелений', '#00ff00'))
btn_green.pack(fill='x')

btn_blue = Button(root, bg="#007dff", command=lambda: get_color('Голубий', '#007dff'))
btn_blue.pack(fill='x')

btn_dark_blue = Button(root, bg="#0000ff", command=lambda: get_color('Синій', '#0000ff'))
btn_dark_blue.pack(fill='x')

btn_violet = Button(root, bg="#7d00ff", command=lambda: get_color('Фіолетовий', '#7d00ff'))
btn_violet.pack(fill='x')

root.mainloop()
