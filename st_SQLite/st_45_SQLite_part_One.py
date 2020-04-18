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

db.close()