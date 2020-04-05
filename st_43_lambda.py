# Звичайна фуекція:
def get_square(num):
    return num ** 2


# Та сама функція, але реалізована через lambda
get_square = lambda num: num ** 2


# Також можна використовувати у такому випадку:
print((lambda num: num ** 2)(7))


# Використання лямбдиу  робочій ситуації.
l = [1, 2, 3] # [2, 4, 6]

# Функція яка в собі виконує прохід по списку-аргументу і кожен елемент опрацбовує лямбдою (через функцію map)
def get_double(l):
    return list(map(lambda num: num * 2, l))


print(get_double(l))