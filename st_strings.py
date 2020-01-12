# **********************************************************************************************************************
# **********************************************************************************************************************
# strings - Lesson 08
words = 'Hello, world!'
words_2 = "Hello, world again!"
# print(words)
# print(words_2)

words_3 = 'Hello, \'Test?\' againe?'
# print(words_3)

words_4 = 'Hello, \\\'Test?\' againe?'
# print(words_4)

verse = 'one \n\
        two '
# print(verse)

verse = '''1
2
3
4'''
# print(verse)


# **********************************************************************************************************************
# **********************************************************************************************************************
# strings - Lesson 09 operations with strings

var = r'c:\d\new.txt'
# print(var)

var1 = 'Python'

var2 = 'Super'

var3 = var1 + ' ' + var2
# print(var3)

name = 'John'
age = 20

# print('My name is ' + name + ', and I have ' + str(age) + ' years old')

# print((name + ' ') * 5)

s = 'Hello world!'
# print(s[0:])

# s[0] = 'd'

# slices
# [x start:y end:z step]

var5 = s
# print(var5[0:12])
# print(var5[0:12:2])
# print(var5[-1])


# **********************************************************************************************************************
# **********************************************************************************************************************
# strings - Lesson 10 methods strings

strOne = 'hello world'
# print(len(strOne)) # длина строки

# print(strOne.capitalize()) # Начинаем с верхнего регистра

# print(strOne.center(20)) # центрирую строку и указываю общую длину символов строки.

# print(strOne.center(25, '*')) # центрирую строку и указываю общую длину символов строки и знак который будет окружать ее

# print(strOne.count('l')) # считаю сколько символов L встречается в строке

# print(strOne.count('l', 0, 3)) # считаю сколько символов L встречается в строке в диапазоне строки от начала до 3-го символа

# print(strOne.find('l')) # Ищу литеру L и вижу индекс первого вхождения. Если символа нет то результат -1

# print(strOne.index('l')) # Ищу литеру L и вижу индекс первого вхождения. Если символа нет то результат ОШИБКА

# print(strOne.replace('l', 'T')) # Заменяю литеру L на литеру Т в строке

# print(strOne.split('l')) # создаем спсиок строк из strOne по ращделителю l. Причем l не будет включена, она просто разделитель

# print(strOne.isdigit()) # Состоит ли строка из цифр (возвращает True или False)

# print(strOne.isalpha()) # Состоит ли строка из букв (возвращает True или False)

# print(strOne.isalnum()) # Состоит ли строка из цифр и букв (возвращает True или False)

# print(strOne.islower()) # Состоит ли строка из символов в нижнем регистре (возвращает True или False)

# print(strOne.isupper()) # Состоит ли строка из символов в верхнем регистре (возвращает True или False)


# **********************************************************************************************************************
# **********************************************************************************************************************
# strings - Lesson 11 format strings
varStr = 'Test string for study'
name = 'John'
age = 30

# print('My name is ' + name + '. ' + 'I\'m ' + str(age))

# print('My name is %(name)s. I\'m %(age)d' %{'name': name, 'age': age}) # старый пример форматирования

# print('My name is %s. I\'m %d' %(name, age)) # второй вариант форматирования строки

'''
%s - строка
%d - число
%f - float
'''

# print('Title: %s, Price: %.2f' %('Sony', 40)) # %s == 'Sony', %.2f == 40 == 40.00. %.2f - float и два символа после запятой

# format:
# print('My name is {}. I\'m {}'.format(name, age)) # Правильный вариант форматирования

# print('My name is {name}. I\'m {age}'.format(name=name, age=age))  # еще вариант использования Format

# f-strings:

# print(f'My name is {name}. I\'m {age}') # самый новый и правильный вариант использования форматирования.

# print(f'My name is {name}. I\'m {age + 5}') #еще варианты использования
#
# Обьединяем элементы списка в строку, с пормощью метода Join
my_list = list(range(1, 10))
my_list_two = list('Hello')

print(my_list, my_list_two) #[1, 2, 3, 4, 5, 6, 7, 8, 9] ['H', 'e', 'l', 'l', 'o']

s = '-'.join(map(str, my_list))# Map: применяем функцию str для каждого эдемента из my_list
print(s) # 1-2-3-4-5-6-7-8-9

s_two = ','.join(my_list_two)# join: для каждого эдемента из my_list_two рязделяем запятой и обьединяем в строку
print(s_two) #H,e,l,l,o

