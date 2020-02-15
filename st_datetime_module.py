# **********************************************************************************************************************
# **********************************************************************************************************************
# Lesson 31 'Datetime Module'
from datetime import date, datetime, timedelta
import locale
print('**************************************************************************************************************')
today = date.today() #возвращает текущую дату
print('1 -->:', today)
# 2020-02-14

print('**************************************************************************************************************')
print('2 -->:', today.day) #возвращает текущее число
# 14

print('**************************************************************************************************************')
print('3 -->:', today.month)#возвращает текущий месяц
# 2

print('**************************************************************************************************************')
print('4 -->:', today.year)#возвращает текущий год
# 2020

print('**************************************************************************************************************')
print('5 -->:', today.weekday())#возвращает день недели (начиная с "0")
# 4

print('**************************************************************************************************************')
# date
# today = date.today()
# print(today) # 2019-07-10
# print(today.day) # 10
# print(today.month) # 7
# print(today.year) # 2019
# print(today.weekday()) # 2019

print('**************************************************************************************************************')
from datetime import datetime

now = datetime.now() # тоже самое что datetime.today
now2 = datetime.today() # тоже самое что datetime.now

print('6 -->:', now)
# 2020-02-14 18:16:27.569347

print('7 -->:', now2)
# 2020-02-14 18:16:27.569347
print('**************************************************************************************************************')
print('8 -->:', now.hour)
# 18

print('**************************************************************************************************************')
print('9 -->:', now.minute)
# 19

print('**************************************************************************************************************')
print('10 -->:', now.min)
# 0001-01-01 00:00:00

print('**************************************************************************************************************')
print('11 -->:', now.second)
# 29

print('**************************************************************************************************************')
print('12 -->:', now.day)
# 15

print('**************************************************************************************************************')
print('13 -->:', now.month)
# 2

print('**************************************************************************************************************')
print('14 -->:', now.year)
# 2020

print('**************************************************************************************************************')
print('15 -->:', now.weekday())
# 5

print('**************************************************************************************************************')
days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'н']
print('16 -->:', days[now.weekday()])
# сб

print('**************************************************************************************************************')
now = datetime.now()
print('17 -->:', now)
# 2020-02-15 14:49:43.938438


print('**************************************************************************************************************')
print('18 -->:', now.strftime('%a'))
# Sat

print('19 -->:', now.strftime('%A'))
# Saturday

print('**************************************************************************************************************')
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')

print('20 -->:', now.strftime('%a'))
# Сб

print('21 -->:', now.strftime('%A'))
# суббота

print('**************************************************************************************************************')
print('22 -->:', f'Дата: {now.strftime("%a, %d, %b, %Y")}')
# Дата: Сб, 15, фев, 2020

print('**************************************************************************************************************')
print('23 -->:', f'Время: {now.strftime("%H:%M:%S")}')
# Время: 15:05:08

print('**************************************************************************************************************')
print('24 -->:', now.strftime("%c"))
#15.02.2020 15:08:23

print('**************************************************************************************************************')
print('25 -->:', now.strftime("%x"))
#15.02.2020

print('**************************************************************************************************************')
print('26 -->:', now.strftime("%X"))
#15:08:23

print('**************************************************************************************************************')
from datetime import timedelta
now = datetime.now()
print('27 -->:', now.strftime('%c'))
# 15.02.2020 15:14:06

print('**************************************************************************************************************')
d1 = now + timedelta(days=1, hours=2, minutes=10)
print('28 -->:', d1)
# 2020-02-16 17:26:24.383866

print('**************************************************************************************************************')
print('29 -->:', d1.strftime('%c'))
# 16.02.2020 17:29:03

print('**************************************************************************************************************')


print('**************************************************************************************************************')
# date
# today = date.today()
# print(today) # 2019-07-10
# print(today.day) # 10
# print(today.month) # 7
# print(today.year) # 2019
# print(today.weekday()) # 2019

# datetime
# now = datetime.now()
# now2 = datetime.today()

# print(now) # 2019-07-10 14:16:51.696373
# print(now.day) # 10
# print(now.month) # 7
# print(now.year) # 2019
# print(now.weekday()) # 2
# print(now.hour) # 14
# print(now.minute) # 16
# print(now.second) # 51

# days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
# print(days[now.weekday()]) # ср

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# locale.setlocale(locale.LC_ALL, 'ru_RU')

# now = datetime.now()
# print(now)
#
# print(now.strftime('%a'))
# print(now.strftime('%A'))
#
# print(f'Дата: {now.strftime("%A, %d %b %Y")}')
# print(f'Время: {now.strftime("%H:%M:%S")}')
#
# print(now.strftime('%c'))
# print(now.strftime('%x'))
# print(now.strftime('%X'))

now = datetime.today()
# print(now.strftime('%c'))
d1 = now + timedelta(days=1, hours=2, minutes=10)
# print(d1.strftime('%c'))



# import random
#
# x = random.randint(1, 100)
# user_num = 0
# cnt = 0
#
# while True:
#     user_num = int(input('Я загадал число от 1 до 100 - угадай его: '))
#     cnt += 1
#     if user_num == x:
#         print(f'Ты угадал число за {cnt} попыток')
#         print("""
#                 ------------
#                 |           |
#                 |  0     0  |
#                 |     <     |
#                 |  .     .  |
#                 |   `...`   |
#                 ------------
#                 """)
#         if input('Сыграем еще? "y|n":') == 'y':
#             x = random.randint(1, 100)
#             cnt = 0
#         else:
#             print('Спасибо за игру')
#             break
#     elif user_num > x:
#         print('Мое число меньше')
#     else:
#         print('Мое число больше')
