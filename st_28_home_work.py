# **********************************************************************************************************************
# **********************************************************************************************************************
# *****Lesson 28 'Home work'

"""
1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный). Определите, есть ли в списке число,
которое является индексом элемента "odd". Напишите функцию, которая будет возвращать True или False, соответсвенно.
"""

def odd_ball(arr):
    def ind(arr):
        # list.index(x, [start [, end]]) - Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
        if 'odd' in arr:
            return arr.index('odd')
        else: pass
    if ind(arr) in arr:
        return True
    else: return False

print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"])) # True
print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"])) # False
print(odd_ball(["even",10,"odd",2,"even"])) # True


"""
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности включительно. 
Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5. Попробуйте решить задачу двумя 
способами (один из способов в одну строчку кода).


def find_sum(n):
    pass

find_sum(5) # return 8 (3 + 5)
find_sum(10) # return 33 (3 + 5 + 6 + 9 + 10)
"""

"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]



def get_names(names):
    pass
    
"""

