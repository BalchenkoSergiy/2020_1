# **********************************************************************************************************************
# **********************************************************************************************************************
# strings - Lesson 13 'FOR', 'WHILE'
'''
var = 1
count = 0
emptyList = []
while var < 10:
    count +=1
    print(count)
    emptyList.append(var)
    var += 1


print(emptyList)
'''

# print изнутри
#print(*objs, sep = '', end = '\n', file = sys.stdout, flush = False)

'''
#sep - разделитель
#end - завершающий символ функции print
print('Hello', 'World', sep = '* *')
'''

'''
var = 'Hallo world!'

for l in var:
    if l == ' ': # если мы находим на пробел то пропускаем и идем дальше
        continue # 
    print(f'"{l}"', end = ' ')

'''

'''
var = 'Hallo world!'

for i in var:
    if i == ' ': # если мы находим на пробел то останавливаемся и прекращаем цикл
        break #
    print(f'"{i}"', end = ' ')
'''

'''
var = 'Hallo world!'

for i in var:
    if i == 's': # если мы находим на пробел то останавливаемся и прекращаем цикл
        break #
    print(f'"{i}"')
else: # если цыкл полностью отработал то else всегда сработает после окончания цикла
    print('Break no worked')
'''

'''
year = 1900
yourYear = int(input('Insert your first year please:'))
endYear = 2019

while yourYear <= 2019:
    print( yourYear, end=', ')
    yourYear += 1
'''
