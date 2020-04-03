from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime


class ParserKorespondent:
    results = []
    now = datetime.now()

    # Передаю посилання на сайт у конструктор при ініціалізації
    def __init__(self, url):
        self.req = urllib.request.urlopen(url)

    # Витягую із сторінки HTML розмітку
    def get_html(self):
        self.html = self.req.read()

    # Для зручного перегляду розпарсюю HTML за допомогою BeautifulSoup і вказую парсер для HTML - 'html.parser'
    def pars_html(self):
        self.soup = BeautifulSoup(self.html, 'html.parser')

    # Відбираю у файлі лише потрібні для мене блоки які містять новини за допомогою методу find_all
    def pars_news(self):
        self.news = self.soup.find_all('div', class_='article')

    # Додаю у список results потрібну мені інформацію із self.news групуючи її по словникам і в кожен словник
    # відбираю таку інформацію: 'Time', 'Title', 'Href'
    def add_in_results(self):
        for item in self.news:
            title = item.find('div', class_='article__title').get_text(strip=True)
            if (item.find('span', class_='article__time')) != None:
                times = item.find('span', class_='article__time').get_text(strip=True)
            href = item.a.get('href')
            self.results.append({
                'Time': times,
                'Title': title,
                'Href': href
            })

    # Записую всі опрацьовані данні у новий файл (із типом запису "перезапис").
    # З початку йде поточний час запиту, потім нумеровані новини і в кінці затрачений час на опрацювання запиту.
    def write_to_log_file(self):
        self.f = open('kor_parser.txt', 'w', encoding='utf-8')
        i = 1
        self.f.write(f'Поточний час: {self.now}\n\n')
        for item in self.results:
            self.f.write(f'\n\nНовина №: {i} \n\n Час новини: {item["Time"]}\n Назва:{item["Title"]}\n Посилання: {item["Href"]}')
            i += 1
        end_time = datetime.now()
        self.f.write(f'Тривалість виконання запиту: \n\n{end_time - (self.now)}')
        self.f.close()

    # Метод який запускає виконання роботи класу у логічній послідовності
    def starter(self):
        self.get_html()
        self.pars_html()
        self.pars_news()
        self.add_in_results()
        self.write_to_log_file()

