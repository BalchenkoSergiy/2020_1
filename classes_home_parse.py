from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime


class ParserKorespondent:
    results = []
    now = datetime.now()

    def __init__(self, url):
        self.req = urllib.request.urlopen(url)

    def get_html(self):
        self.html = self.req.read()

    def pars_html(self):
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def pars_news(self):
        self.news = self.soup.find_all('div', class_='article')

    def add_in_results(self):
        for item in self.news:
            title = item.find('div', class_='article__title').get_text(strip=True)
            if (item.find('span', class_='article__time')) != None:
                times = item.find('span', class_='article__time').get_text(strip=True)
            href = item.a.get('href')
            self.results.append({
                'Time': times,
                'Title': title,
                'href': href
            })

    def write_to_log_file(self):
        self.f = open('kor_parser.txt', 'w', encoding='utf-8')
        i = 1
        self.f.write(f'Текущее время запроса: {self.now}\n\n')
        for item in self.results:
            self.f.write(f'Новость №: {i} \n\n Время: {item["Time"]}\n Название:{item["Title"]}\n Ссылка: {item["href"]}')
            i += 1
        end_time = datetime.now()
        self.f.write(f'Длительность выполнения: \n\n{end_time - (self.now)}')
        self.f.close()

    def starter(self):
        self.get_html()
        self.pars_html()
        self.pars_news()
        self.add_in_results()
        self.write_to_log_file()

