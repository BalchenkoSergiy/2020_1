# Імпортую модуль sqlite3
import sqlite3

# Створюю БД (якщо вона вже є, то я конекчусь до неї)
db = sqlite3.connect('my_db.db')
# Створюю cursor для подальших запитів до нашої БД
cursor = db.cursor()

# Створюю таблицю users
#cursor.execute('''
#    CREATE TABLE users (
#        id INTEGER PRIMARY KEY,
#        name TEXT NOT NULL,
#        email TEXT NOT NULL UNIQUE)
#    ''')

# Вставляю данні у таблицю users
#cursor.execute('''
#    INSERT INTO users (name, email)
#        VALUES
#            ('Petrov Petr', 'petrov@com'),
#            ('Sidorov Oleg', 'sidorov@com')
#    ''')
#db.commit()

# Якщо мені потрібно створити два запити в одному кейсі то я використовую executescript
#cursor.executescript('''
#    INSERT INTO users (name, email)
#        VALUES
#            ('Stallone Silvester', 'stallone@com');
#    INSERT INTO users (name, email)
#        VALUES
#            ('Lee Brandon', 'lee@com');
#    ''')
#db.commit()

# Створюю список кортежей із юзерами для подальшого використання методу executemany()
users = [
    ('User_1', 'user_1@gmail.com'),
    ('User_2', 'user_2@gmail.com'),
    ('User_3', 'user_3@gmail.com')
]

# Тепер із-за допомогою методу executemany() я вставляю у таблицю одразу цілу колекцію
#cursor.executemany('''
#    INSERT INTO users (name, email)
#        VALUES
#            (?, ?)''', users
#    )
#db.commit()

# Для отримання данних із таблиці:
email = 'petrov@com'

# Записую свій SELECT
cursor.execute('''
    SELECT * FROM users WHERE email = ?
    ''', (email,))
# Для отримання одного запису використовую метод fetchone() і записую результат у змінну result
result = cursor.fetchone()

#print(result)# (2, 'Petrov Petr', 'petrov@com')
#print(result[1])# Petrov Petr
#print(result[2])# petrov@com


# Можна ускладнити запит умовою:
cursor.execute('''
    SELECT * FROM users WHERE email = :email OR name = :name
    ''', {'email': email, 'name': 'John Doe'})

result = cursor.fetchone()

#print(result)# (2, 'Petrov Petr', 'petrov@com')
#print(result[1])# Petrov Petr
#print(result[2])# petrov@com

# Для отримання всіх записів використовую метод fetchall() і записую результат у змінну result.
# Даний метод повертає список кортежей із даними в таблиці
cursor.execute('''
    SELECT * FROM users 
    ''')

result = cursor.fetchall()

# print(result)
# [(1, 'Ivanov Ivan', 'ivanov@com'), (2, 'Petrov Petr', 'petrov@com'), (3, 'Sidorov Oleg', 'sidorov@com'), (4, 'Stallone Silvester', 'stallone@com'), (5, 'Lee Brandon', 'lee@com'), (6, 'User_1', 'user_1@gmail.com'), (7, 'User_2', 'user_2@gmail.com'), (8, 'User_3', 'user_3@gmail.com')]

# Для зручного виводу:
#for user in result:
#    print(user[1], user[2])
'''
Ivanov Ivan ivanov@com
Petrov Petr petrov@com
Sidorov Oleg sidorov@com
Stallone Silvester stallone@com
Lee Brandon lee@com
User_1 user_1@gmail.com
User_2 user_2@gmail.com
User_3 user_3@gmail.com
'''

# Для отримання результату у вигляді словника:
# Створюю функцію яка повертає данні у вигляді словника:
def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d

# Прив'язую дану функцію до курсору:
db.row_factory = dict_factory
cursor = db.cursor()

# Створюю запит:
cursor.execute('''
    SELECT * FROM users''')
result = cursor.fetchall()

print(result)
#[{'id': 1, 'name': 'Ivanov Ivan', 'email': 'ivanov@com'}, {'id': 2, 'name': 'Petrov Petr', 'email': 'petrov@com'}, {'id': 3, 'name': 'Sidorov Oleg', 'email': 'sidorov@com'}, {'id': 4, 'name': 'Stallone Silvester', 'email': 'stallone@com'}, {'id': 5, 'name': 'Lee Brandon', 'email': 'lee@com'}, {'id': 6, 'name': 'User_1', 'email': 'user_1@gmail.com'}, {'id': 7, 'name': 'User_2', 'email': 'user_2@gmail.com'}, {'id': 8, 'name': 'User_3', 'email': 'user_3@gmail.com'}]
db.close()