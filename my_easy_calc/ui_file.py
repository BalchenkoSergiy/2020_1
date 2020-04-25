from tkinter import *
from tkinter import ttk
from my_easy_calc.classes import *
task = {'x': x(), 'y': y()}
obj_class = Calc(task['x'], task['y'])

# Створюю змінну яка буде об'єктом Tk()
root = Tk()

# Підписую назву вікна (на подобі title в HTML)
root.title('My calc')


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

root.title('My little calc')

my_button_x = ttk.Button(root, text=f'{obj_class.x}')
my_button_x.pack()

my_button_y = ttk.Button(root, text=f'{obj_class.y}')
my_button_y.pack()

my_button_plus = ttk.Button(root, text=' + ', command=obj_class.plus)
my_button_plus.pack()

my_button_minus = ttk.Button(root, text=' - ', command=obj_class.minus)
my_button_minus.pack()

my_button_divided = ttk.Button(root, text=' / ', command=obj_class.divided)
my_button_divided.pack()

my_button_multiply = ttk.Button(root, text=' * ', command=obj_class.multiply)
my_button_multiply.pack()

def counter():
    my_button_result = ttk.Button(root, text=f'Result = {obj_class.result}')
    my_button_result.pack()


btn_cnt = Button(root, text=" = ", command=counter)
btn_cnt.pack()


# Використовую метод mainloop() який запускає цикл відображення вікна.
root.mainloop()




