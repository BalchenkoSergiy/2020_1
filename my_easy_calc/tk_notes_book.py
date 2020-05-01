# Імпортую модуль
import tkinter
# Імпортую більш сучасний набір елементів управління
import tkinter.ttk
# Імпортую модуль для виводу вікна сповіщень
import tkinter.messagebox

# Оприділяю класс Application - контейнер, який формує зміст вікна додатку
class Application(tkinter.ttk.Frame):
    '''
    Как правило, в качестве контейнера используется класс, являющийся производным от класса  Frame  из модуля
    tkinter.ttk  (отметим, что это новый, стилизуемый контейнер).  Frame — это просто серая панель.
    '''
    def __init__(self,  master=None):
        super() .__init__(master)
        self .pack()
        self.create_widgets()
        self.master.title("Test")
        self.master.resizable(False,  False)

    # Створення компонентів вікна
    def create_widgets(self):
        # Створення кнопки (опция text компонента кнопки (Button) задает текст надписи на кнопке)
        # Отметим, что текст для надписи мы разбили на две строки, использовав специальный символ "\n".
        # Практически все компоненты библиотеки Tkinter позволяют это сделать.
        self.btnHello = tkinter.ttk.Button(self, text="Приветствовать\nпользователя")
        # Напишем  выражение,  привязывающее  к  событию  ButtonRelease  в  качестве  обработчика
        # метод  say hello  ()  класса  Application:
        self.btnHello.bind("<ButtonRelease>", self.say_hello)
        # Воспользуемся диспетчером компоновки Pack, который располагает компоненты вдоль границ
        # контейнера. Вероятно, это самая простая и быстродействующая из подсистем подобного рода
        # Метод pack(), вызванный без параметров у нашей кнопки, поместит ее в месторасположение по
        # умолчанию — вдоль верхнего края контейнера-родителя.
        self.btnHello.pack()
        # Создадим вторую кнопку
        self.btnShow = tkinter.ttk.Button(self)
        # Создадим надпись на кнопке вторым способом
        self.btnShow["text"] = "Выход"
        self.btnShow["command"] = root.destroy
        self.btnShow.pack(side="bottom")

    # Метод  say hello  ()  будет вызван после щелчка на кнопке "self.btnHello.bind"
    # и выведет на экран окно сообщение.
    def say_hello(self, evt):
        tkinter.messagebox.showinfo("Test",  "Привет,  пользователь!")

root = tkinter.Tk()
app = Application(master=root)
root.mainloop()