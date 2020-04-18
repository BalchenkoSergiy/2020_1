from bs4 import BeautifulSoup
import urllib.request

# Открываю нужный мне сайт с помощью urllib.request.urlopen
req = urllib.request.urlopen('https://ua.korrespondent.net/')

# Возвращаю html код страницы и присваиваю его в переменную
html = req.read()

# Использую модуль BeautifulSoup для роспарсения переменной html с помощью метода html.parser для удобства читаемости
soup = BeautifulSoup(html, 'html.parser')

# Роспарсиваю переменную soup отбирая только блок новостей
news = soup.find_all('div', class_='article')

# Переменная которая будет состоять из списка словарей из набором нужных мне данных по каждой новости
results = []

# Проходя цыклом по отобраной информацыи я обрезаю названия тегов и пробелы по сторонам. В конце добавляю результ в словари из results
for item in news:
    title = item.find('div', class_='article__title').get_text(strip=True)
    if (item.find('span', class_='article__time')) != None:
        times = item.find('span', class_='article__time').get_text(strip=True)
    href = item.a.get('href')
    results.append({
        'Time': times,
        'Title': title,
        'href': href
    })

# Теперь записываю все в файл txt который создаю:
f = open('home_work_1_04.txt', 'w', encoding='utf-8')

i = 1

for item in results:
    f.write(f'Новость №: {i} \n\n Время: {item["Time"]}\n Название:{item["Title"]}\n Ссылка: {item["href"]}')
    i += 1
f.close()
