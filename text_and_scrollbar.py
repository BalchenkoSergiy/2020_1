from tkinter import *

root = Tk()
root.geometry('600x400+3000+300')

# Создаю фрейм для меню из высотой 40 и с фоновым цветом #1F252A
f_menu = Frame(root, bg="#1F252A", height=40)
f_menu.pack(fill=X)

# Фрейм для области ввода текста
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

# Размещаю во фрейме f_menu лейбл для дальнейшей работы с меню
l_menu = Label(f_menu, text="Menu", bg="#2B3239", fg="#C6DEC1", font="Arial 10")
l_menu.place(x=10, y=10)

# Размещаю виджет для ввода текста Text внутрь фрейма f_text
# bg - фоновый цвет
# fg - цвет текста
# padx, pady - отступы текста от граней окна ввода
# wrap - свойство переноса на следующую строку. WORD не дает обрезать слова и переносит их целиком
# insertbackground - цвет курсора
# selectbackground - цвет выделеного цвета
# spacing1, spacing2, spacing3 - разные отступы между строками
t = Text(f_text, bg="#343D46", fg="#C6DEC1", padx=10, pady=10, wrap=WORD, insertbackground="#EDA756",
    selectbackground="#4E5A65", width=30, spacing3=5)
t.pack(fill=BOTH, expand=1, side=LEFT)


# Создаю переменную "scroll" из типом "Scrollbar" и привязываю ее к фрейму  "f_text" по оси Y "command=t.yview"
scroll = Scrollbar(f_text, command=t.yview)
# Размещаю наш скрол что бы он тянулся по оси Y "fill=Y", и размещаю слева от редактора "side=LEFT"
scroll.pack(fill=Y, side=LEFT)
# Вставляем наш встроеный скрол
t.config(yscrollcommand=scroll.set)

# Функция которая вставляет "'Hello!" во 2-ую строчку и на индекс 4 (строки считаем с 1 а индексы с 0)
def add_str():
    t.insert('2.4', 'Hello!')


# Функция которая удаляет указаный срез символов
def del_str():
    # t.delete('2.4', '2.10')
    t.delete('1.0', END)

# Функция которая копирует текст в указаном срезе
def get_str():
    print(t.get('1.0', END))


# Создаю кнопки и привязываю их к нужным функциям
btn_add = Button(root, text="Add", command=add_str).place(x=80, y=10)
btn_del = Button(root, text="Delete", command=del_str).place(x=120, y=10)
btn_get = Button(root, text="Get", command=get_str).place(x=170, y=10)


root.mainloop()

'''
Виджет ТЕХТ дает возможность вводить многострочные строки. В отличии от виджета Entry
'''