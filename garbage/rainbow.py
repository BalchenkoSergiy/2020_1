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

colors = {
    '#ff0000': 'Червоний',
    '#ff7d00': 'Оранжевий',
    '#ffff00': 'Жовтий',
    '#00ff00': 'Зелений',
    '#007dff': 'Голубий',
    '#0000ff': 'Синій',
    '#7d00ff': 'Фіолетовий',
}


class MyButtons:
    def __init__(self, master, text_color, code_color):
        self.text_color = text_color
        self.code_color = code_color
        self.but = Button(master, bg=code_color, command=self.get_color)
        self.but.pack(fill='x')

    def get_color(self):
        label['text'] = self.text_color
        self.but['text'] = self.text_color
        entry.delete(0, END)
        entry.insert(0, self.code_color)


label = Label(root)
label.pack()

entry = Entry(root, width=30, justify='center')
entry.pack()

for k, v in colors.items():
    MyButtons(root, v, k)

root.mainloop()
