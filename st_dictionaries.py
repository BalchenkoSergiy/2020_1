# **********************************************************************************************************************
# **********************************************************************************************************************
# *****Lesson 23 'Dictionaries'

d = {}
print('1-->', type(d))# <class 'dict'>

print('***************************************************************************************************************')
product1 = {'title': 'Sony',
            'price': 100}
product2 = dict(title='iPhone',
                price=110)

print('2-->', product1)# {'title': 'Sony', 'price': 100}
print('3-->' ,product2)# {'title': 'iPhone', 'price': 110}

print('***************************************************************************************************************')
#Создаем словарь из списка или кортежа
users = [
     ['bob@gmail.com', 'Bob'],
     ['katy@gmail.com', 'Katy'],
     ['john@gmail.com', 'John']
 ]
d_users = dict(users)
print('4-->', users)# [['bob@gmail.com', 'Bob'], ['katy@gmail.com', 'Katy'], ['john@gmail.com', 'John']]
print('5-->', d_users)# {'bob@gmail.com': 'Bob', 'katy@gmail.com': 'Katy', 'john@gmail.com': 'John'}

print('***************************************************************************************************************')
users_t = (
     ('bob@gmail.com', 'Bob'),
     ('katy@gmail.com', 'Katy'),
     ('john@gmail.com', 'John')
)
t_users = dict(users_t)
print('6-->', users_t)# (('bob@gmail.com', 'Bob'), ('katy@gmail.com', 'Katy'), ('john@gmail.com', 'John'))
print('7-->', t_users)# {'bob@gmail.com': 'Bob', 'katy@gmail.com': 'Katy', 'john@gmail.com': 'John'}

print('***************************************************************************************************************')
product3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)
print('8-->', product3)# 8--> {'price1': 50, 'price2': 50, 'price3': 50}

print('***************************************************************************************************************')
# Используем генератор для создания словаря
nums = {i: i + 1 for i in range(1, 10)}
print('9-->', nums)# 9--> {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}

print('***************************************************************************************************************')
#print(nums['1']) # error
print('10-->', nums[1]) # 2

print('***************************************************************************************************************')
# Выводим значение по ключу, но обходим ошибки
product1 = {'title': 'Sony', 'price': 100}
product2 = dict(title='iPhone', price=110)

print('11-->', product1['price'])# 100
print('12-->', product1.get('price2', 'NO')) # if no key

print('***************************************************************************************************************')
# перебираем словарь
for key in product1:
    print('13-->', f'{key}: {product1[key]}')   # title: Sony
                                                # price: 100

print('***************************************************************************************************************')
# Возвращаем пары "Ключь - Значения"
for key, value in product1.items():
    print('14-->', key, value)  # title Sony
                                # price 100

print('***************************************************************************************************************')
# Используем список словарей
products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 110},
    {'title': 'Samsung', 'price': 90}
]
print('15-->', products) # [{'title': 'Sony', 'price': 100}, {'title': 'iPhone', 'price': 110}, {'title': 'Samsung', 'price': 90}]

print('***************************************************************************************************************')
for product in products:
    print('16-->', product['title'], product['price'])  # Sony 100
                                                        # iPhone 110
                                                        # Samsung 90

