from tkinter import *
from tkinter import ttk
from my_easy_calc.classes import Calc
from my_easy_calc.logic import *

# Створюю змінну яка буде об'єктом Tk()
root = Tk()

# Підписую назву вікна (на подобі title в HTML)
root.title('My first GUI app')


# Я можу управляти позицією вікна появлення то його розмірами
# На подобі осі координат вказую параметри (Нульова точка у верхньому, лівому куті екрану)
# 600 - розмір вікна по ширині
# 400 - розмір вікна по висоті
# 3100 - відступ при появленні вікна з ліва
# 150 - відступ при появленні вікна зверху
root.geometry('1000x800+500+150')

# Я можу управляти можливістю змінювати розмір вікна користувачем:
# Метод resizable дає можливість забороняти міняти (висоту, ширину) якщо поставити False у відповідному місці
root.resizable(False, False)

# Можу змінити фоновий коляр вікна
root.config(bg='grey')

# Для створення стилю кнопки я імпортую із бібліотеки tkinter модуль TTK

my_button_x = ttk.Button(root, text=f'{obj_class.x}')
my_button_x.pack()

my_button_y = ttk.Button(root, text=f'{obj_class.y}')
my_button_y.pack()

my_button_plus = ttk.Button(root, text=f' + ', command=obj_class.plus)
my_button_plus.pack()

my_button_minus = ttk.Button(root, text=f' - ', command=obj_class.minus)
my_button_minus.pack()

my_button_divided = ttk.Button(root, text=f' / ', command=obj_class.divided)
my_button_divided.pack()

my_button_multiply = ttk.Button(root, text=f' * ', command=obj_class.multiply)
my_button_multiply.pack()

my_button_result = ttk.Button(root, text=obj_class.status)
my_button_result.pack()




# Я можу керувати шрифтом тексту кнопки
my_button_5 = Button(root, text='Моя кнопка 5 (font="Arial 20")',  font='Arial 20')
my_button_5.pack()

# Курсивний текст за допомогою шрифту italic
my_button_6 = Button(root, text='Моя кнопка 6 (italic)',  font='Arial 20 italic')
my_button_6.pack()

# Якщо назва шрифта складається із декількох слів я цей параметр передаю у вигляді кортежу:
my_button_7 = Button(root, text='Моя кнопка 7 (Comic Sans MS)', font=('Comic Sans MS',  20))
my_button_7.pack()

# А також я можу використовувати не конструктор а інший методом:
my_button_8 = Button(root, text='Моя кнопка 8 (configure)')
my_button_8.configure(width=20, height=5)
my_button_8['font'] = 'Arial 15'
my_button_8.pack()



# Використовую метод mainloop() який запускає цикл відображення вікна.
root.mainloop()