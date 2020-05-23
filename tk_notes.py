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

# Додаю якийсь малюнок (це може бути якийсь логотип) у наше вікно:
# 1. Створюю змінну і за допомогою мітки PhotoImage прив'язую її до якоїсь картинки
img = PhotoImage(file='img/pngguru.png')

# 2. Створюю Label який прив'язую до змінної із малюнком
pic_logo = Label(root, image=img, width='700', height='20')

# 3. Розміщую віджет-малюнок у мому вікні із допомогою методу Pack
pic_logo.pack()


# Створюю напис у вікні використовуючи метод Label
lab_text = Label(root,
                 text=f'Тестовий текст у вікні\nякий буде відображатись по замовчуванню\nі не підлягатиме редагуванню',
                 bg='white',
                 # width='80',
                 # height='5',
                 font=("Comic Sans MS", 10, "bold"),
                 anchor='center')
# anchor може приймати такі значення:
# n - верх, середина
# ne - верх, право
# e - середина, право
# se - низ, право
# s - низ, середина
# sw - низ, ліво
# w - середина, ліво
# nw - верх, ліво
# center - центр

# Розміщую віджет-текс у мому вікні із допомогою методу Pack
lab_text.pack()

# Створюю текст (label) та поле для вводу за допомогою (Entry)
l_test_text = Label(root, text='Insert something:')
l_test_text.pack(side='right', anchor='nw')

e_entry = Entry(root, bd=5)
e_entry.pack(anchor='ne')

# Створюю кнопку
my_button = Button(root, text='Моя кнопка')

# Розміщую віджет-кнопку у мому вікні із допомогою методу Pack
my_button.pack(side=TOP, anchor='nw')

# Це саме можна зробити і у одній строці (Але бажано перший варіант використовувати):
my_button_2 = Button(root, text='Моя кнопка 2').pack(side=TOP, anchor='nw')

# Для створення стилю кнопки я імпортую із бібліотеки tkinter модуль TTK
# Тепер створюючи кнопку я використовую метод TTK:
my_button_3 = ttk.Button(root, text='Моя кнопка 3')
my_button_3.pack(side=TOP, anchor='nw')

# Створюю функцію яка просто щось виводить у консоль:
def clicked():
    print('Clicked')

# Тепер зв'язую функцію із кнопкою за допомогою параметру command
my_button_4 = Button(root, text='Моя кнопка 4 (def clicked)', command=clicked)
my_button_4.pack(side=TOP, anchor='nw')

# Я можу керувати шрифтом тексту кнопки
my_button_5 = Button(root, text='Моя кнопка 5 (font="Arial 8")', command=clicked, font='Arial 8')
my_button_5.pack(side=TOP, anchor='nw')

# Курсивний текст за допомогою шрифту italic
my_button_6 = Button(root, text='Моя кнопка 6 (italic)', command=clicked, font='Arial 10 italic')
my_button_6.pack(side=TOP, anchor='nw')

# Якщо назва шрифта складається із декількох слів я цей параметр передаю у вигляді кортежу:
my_button_7 = Button(root, text='Моя кнопка 7 (Comic Sans MS)', command=clicked, font=('Comic Sans MS',  10))
my_button_7.pack(side=TOP, anchor='nw')

# А також я можу використовувати не конструктор а інший методом:
my_button_8 = Button(root, text='Моя кнопка 8 (configure)')
my_button_8.configure(width=20, height=0)
my_button_8['font'] = 'Arial 10'
my_button_8.pack(side=TOP, anchor='nw')

# Створюю кнопку яка при нажатті показує поточний час. Для цього:
# 1. Імпортую модуль Time
# 2. Створюю функцію яка викликає поточний час та називає мою кнопку цими данними
def check_time():
    btn_time_9['text'] = time.strftime('%H:%M:%S')

# 3. Прив'язую кнопку до функції:
btn_time_9 = Button(root, text="Моя кнопка 9 (поточний час)", command=check_time)
btn_time_9.pack(side=TOP, anchor='nw')

# Створюю кнопку яка рахує кількість кліків. Для цього:
# 1. Стфорюю змінну яка буде лічильником:
clicks = 0

# 2. Створюю функцію яка додає до глобальної змінної +1 та називає результат вичислення у title вікна:
def counter():
    global clicks
    clicks += 1
    root.title(f'Total clicks = {clicks}')

# 3. Створюю кнопку 10 при нажатті на яку викликається функція counter:
btn_cnt = Button(root, text="Моя кнопка 10 (кількість кліків)", command=counter)
btn_cnt.pack(side=TOP, anchor='nw')

# activebackground - змінює коляр фону натиснутої кнопки
my_button_11 = Button(root, text="Моя кнопка 11 (activebackground)", command=counter, activebackground='Green')
my_button_11.pack(side=TOP, anchor='nw')

# activeforeground - змінює коляр тексту натиснутої кнопки
my_button_12 = Button(root, text="Моя кнопка 12 (activebackground)", command=counter, activeforeground='Green')
my_button_12.pack(side=TOP, anchor='nw')

# bd - змінює змінює ширину рамки кнопки (по замовчуванню = 2)
my_button_13 = Button(root, text="Моя кнопка 13 (bd)", command=counter, bd=5)
my_button_13.pack(side=TOP, anchor='nw')

# bg - встановлює коляр фону не нажатої кнопки
my_button_14 = Button(root, text="Моя кнопка 14 (bg)", command=counter, bg='green')
my_button_14.pack(side=TOP, anchor='nw')

# fg - встановлює коляр тексту не нажатої кнопки
my_button_15 = Button(root, text="Моя кнопка 15 (fg)", command=counter, fg='green')
my_button_15.pack(side=TOP, anchor='nw')

# fg - встановлює коляр тексту не нажатої кнопки active, disabled, or normal
my_button_16 = Button(root, text=f"Моя кнопка 16\nNew_Row", command=counter, width=80, relief='ridge')
my_button_16.pack(side=TOP, anchor='nw')

# Використовую метод mainloop() який запускає цикл відображення вікна.
root.mainloop()




