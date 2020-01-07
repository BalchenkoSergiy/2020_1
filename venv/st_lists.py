# **********************************************************************************************************************
# **********************************************************************************************************************
# Lesson 14 'Lists'
my_list = [1, 2, 3, 'hello', ['test', 10], 'world', True] # [1, 2, 3, 'hello', ['test', 10], 'world', True]
print(my_list)
print('************************************************************')

my_list = list('hello') # ['h', 'e', 'l', 'l', 'o']
print(my_list)
print('************************************************************')

my_list = list((1, 2, 3)) # [1, 2, 3]
print(my_list)
print('************************************************************')

my_list = [i for i in 'hello'] # ['h', 'e', 'l', 'l', 'o']
print(my_list)
print('************************************************************')

my_list = [i for i in 'hello world' if i != ' '] # ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
print(my_list)
print('************************************************************')

my_list = [i for i in 'hello world' if i not in ['a', 'e', ' ', 'i', 'o']] # ['h', 'l', 'l', 'w', 'r', 'l', 'd']
print(my_list)
print('************************************************************')

my_list = [i for i in range (3)] # [0, 1, 2]
print(my_list)
print('************************************************************')

my_list = [i for i in range (3, 9)] # [3, 4, 5, 6, 7, 8]
print(my_list)
print('************************************************************')

my_list = [i for i in range (3, 9, 2)] # [3, 5, 7]
print(my_list)
print('************************************************************')

print(list(range(0, 11, 2))) # [0, 2, 4, 6, 8, 10]
print('************************************************************')

for i in range(1, 3):
    print(f'Внешний цикл #{i}')
    for j in range (1, 3):
        print(f'\tВнутренний цикл #{j}')

print('************************************************************')

my_list_first = [i for i in range (0, 10)]
my_list_second = [i for i in range (0, 10)]

for i in range(0, 10):
    print('--->', end=' ')
    for s in my_list_second:
        print(f'{my_list_first[i]} * {s} = {my_list_first[i] * s}\t', end=' ')
    print(' ')
print('************************************************************')

# **********************************************************************************************************************
# **********************************************************************************************************************
# Lesson 16 'Lists'

my_list = [1, 2, 3, 'hello', ['test', 10], 'world', True]
mylist_names = ['Ivanov', 'Petrov', 'Sidorov']

print(my_list[4][0]) # test
print(my_list[0:3]) # [1, 2, 3]

print('************************************************************')
my_list = [1, 2, 3, 'hello', ['test', 10], 'world', True]
my_list[2] = 'world'
print(my_list) # [1, 2, 'world', 'hello', ['test', 10], 'world', True]

print('************************************************************')
my_list = [1, 2, 3, 'hello', ['test', 10], 'world', True]
my_list[:2] = [10, 15]
print(my_list) # [10, 15, 3, 'hello', ['test', 10], 'world', True]

print('************************************************************')
# list.append(x) - Добавляет элемент в конец списка
my_list = [1, 2, 3, 'hello', ['test', 10], 'world', True]
my_list.append('new')
print(my_list) # [1, 2, 3, 'hello', ['test', 10], 'world', True, 'new']

print('************************************************************')
# list.extend(L) - Расширяет список list, добавляя в конец все элементы списка L
my_list = [1, 2, 3, 'hello', ['test', 10], 'world', True]
my_list.extend([5, 7])
print(my_list) # [1, 2, 3, 'hello', ['test', 10], 'world', True, 5, 7]

print('************************************************************')
# list.insert(i, x) - Вставляет на i-ый элемент значение x
my_list = [1, 2, 3, 'hello', ['test', 10], 'world', True]
my_list.insert(1, 'test')
print(my_list) # [1, 'test', 2, 3, 'hello', ['test', 10], 'world', True]

print('************************************************************')
# list.remove(x) - Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
my_list = [1, 2, 3, 'hello', ['test', 10], 'world', True]
my_list.remove('world')
print(my_list) # [1, 2, 3, 'hello', ['test', 10], True]

print('************************************************************')
# list.pop([i]) - Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
my_list = [1, 2, 3, 'hello', ['test', 10], 'world', True]
my_list.pop()
print(my_list) # [1, 2, 3, 'hello', ['test', 10], 'world']

my_list = [1, 2, 3, 'hello', ['test', 10], 'world', True]
my_list.pop(3)
print(my_list) # [1, 2, 3, ['test', 10], 'world', True]

print('************************************************************')
# list.index(x, [start [, end]]) - Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
my_list = [1, 2, 3, 'hello', ['test', 10], 'world', True]
print(my_list.index('hello')) # 3

print('************************************************************')
# list.count(x) - Возвращает количество элементов со значением x
my_list = [1, 2, 3, 'hello', ['test', 10], 'world', True]
print(my_list.count('hello')) # 1

print('************************************************************')
# list.sort([key=функция], [reverse=False]) - Сортирует список на основе функции (элементы должны быть однотипные)
my_list = ['ali', 'hello', 'hi', 'world', 'test']
my_list.sort()
print(my_list) # ['ali', 'hello', 'hi', 'test', 'world']

my_list.sort( reverse=True)
print(my_list) # ['world', 'test', 'hi', 'hello', 'ali']
print('************************************************************')
# list.reverse() - Разворачивает список
my_list = ['ali', 'hello', 'hi', 'world', 'test']
my_list.reverse()
print(my_list) # ['test', 'world', 'hi', 'hello', 'ali']

print('************************************************************')
# list.copy() - Возвращает копию списка
my_list = ['ali', 'hello', 'hi', 'world', 'test']
my_list_three = my_list.copy()
print(my_list_three) # ['ali', 'hello', 'hi', 'world', 'test']

print('************************************************************')
# list.clear() - Очищает список
my_list = ['ali', 'hello', 'hi', 'world', 'test']
my_list.clear()
print(my_list) # []


print('************************************************************')






