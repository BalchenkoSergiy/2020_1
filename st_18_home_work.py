"""
1. Дан список. Получите новый список, в котором каждое значение будет удвоено:
[1, 2, 3] --> [2, 4, 6]
"""
my_list = [1, 2, 3]
result_list = []
for i in my_list:
    i = i * 2
    result_list.append(i)

print('Task 1 --->', result_list)

"""
2. Дан список. Возведите в квадрат каждый из его элементов и получит сумму всех полученных квадратов:
[1, 2, 3] --> 14 --> 1^2 + 2^2 + 3^2 = 14
"""
my_list = [1, 2, 3]
result_list = []
for i in my_list:
    i = i ** 2
    result_list.append(i)

print('Task 2 --->', result_list, f' Sum all elements = {sum(result_list)}')


"""
3. Игорь любит кататься на велосипеде. Он знает, что при этом важно не допустить 
обезвоживания и пьет 0,5 литра воды в час. Вам дается время в часах, и вам нужно
вернуть количество литров, которые Игорь выпьет, с округлением до наименьшего значения.

time1 = 3 --> litres = 1
time2 = 6.7 --> litres = 3
time3 = 11.8 --> litres = 5
"""
my_list_hours = [3, 6.7, 11.8]
my_list_result = []

for i in my_list_hours:
    i = int(i * 0.5)
    my_list_result.append(i)

print('Task 3a --->', my_list_result)

my_list_result = [int(i * 0.5) for i in my_list_hours]
print('Task 3b --->', my_list_result)

"""
4. Дана строка 'Hello world'. Проверьте, если в этой строке есть символ пробела - " ", 
тогда преобразуйте строку к верхнему регистру, если же нет, тогда к нижнему.
***************
s = 'Hello world'
if stm:
	pass
else:
	pass
"""
s = 'Hello world'

if ' ' in s:
    s = s.upper()
else:
    s = s.lower()

print('Task 4 --->', s)