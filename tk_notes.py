# Імпортую модуль tkinter
from tkinter import *
from tkinter import ttk
import time

# Створюю змінну яка буде об'єктом Tk()
root = Tk()

# Підписую назву вікна (на подобі title в HTML)
root.title('My first GUI app')

# Змінюю логотип вікна
# root.iconbitmap('img\png5.ico')

# Я можу управляти позицією вікна появлення то його розмірами
# На подобі осі координат вказую параметри (Нульова точка у верхньому, лівому куті екрану)
# 600 - розмір вікна по ширині
# 400 - розмір вікна по висоті
# 3100 - відступ при появленні вікна з ліва
# 150 - відступ при появленні вікна зверху
root.geometry('800x600+3000+150')

# Я можу управляти можливістю змінювати розмір вікна користувачем:
# Метод resizable дає можливість забороняти міняти (висоту, ширину) якщо поставити False у відповідному місці
root.resizable(True, True)

# Можу змінити фоновий коляр вікна
root.config(bg='grey')

# Створюю кнопку
my_button = Button(root, text='Моя кнопка')

# Розміщую віджет-кнопку у мому вікні із допомогою методу Pack
my_button.pack()

# Це саме можна зробити і у одній строці (Але бажано перший варіант використовувати):
my_button_2 = Button(root, text='Моя кнопка 2').pack()

# Для створення стилю кнопки я імпортую із бібліотеки tkinter модуль TTK
# Тепер створюючи кнопку я використовую метод TTK:
my_button_3 = ttk.Button(root, text='Моя кнопка 3')
my_button_3.pack()

# Створюю функцію яка просто щось виводить у консоль:
def clicked():
    print('Clicked')

# Тепер зв'язую функцію із кнопкою за допомогою параметру command
my_button_4 = Button(root, text='Моя кнопка 4 (def clicked)', command=clicked)
my_button_4.pack()

# Я можу керувати шрифтом тексту кнопки
my_button_5 = Button(root, text='Моя кнопка 5 (font="Arial 20")', command=clicked, font='Arial 20')
my_button_5.pack()

# Курсивний текст за допомогою шрифту italic
my_button_6 = Button(root, text='Моя кнопка 6 (italic)', command=clicked, font='Arial 20 italic')
my_button_6.pack()

# Якщо назва шрифта складається із декількох слів я цей параметр передаю у вигляді кортежу:
my_button_7 = Button(root, text='Моя кнопка 7 (Comic Sans MS)', command=clicked, font=('Comic Sans MS',  20))
my_button_7.pack()

# А також я можу використовувати не конструктор а інший методом:
my_button_8 = Button(root, text='Моя кнопка 8 (configure)')
my_button_8.configure(width=20, height=5)
my_button_8['font'] = 'Arial 15'
my_button_8.pack()

# Створюю кнопку яка при нажатті показує поточний час. Для цього:
# 1. Імпортую модуль Time
# 2. Створюю функцію яка викликає поточний час та називає мою кнопку цими данними
def check_time():
    btn_time_9['text'] = time.strftime('%H:%M:%S')

# 3. Прив'язую кнопку до функції:
btn_time_9 = Button(root, text="Моя кнопка 9 (поточний час)", command=check_time)
btn_time_9.pack()





# Використовую метод mainloop() який запускає цикл відображення вікна.
root.mainloop()