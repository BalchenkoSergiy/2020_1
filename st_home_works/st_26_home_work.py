# Дан список. Получите новый список, в котором каждое значение будет удвоено:
# [1, 2, 3] --> [2, 4, 6]


my_list = [1, 2, 3]

def double_list(us_list):
    result_list = [i*2 for i in us_list]
    return result_list

print('Task 1 --->', double_list(my_list))

"""
Игорь любит кататься на велосипеде. Он знает, что при этом важно не допустить 
обезвоживания и пьет 0,5 литра воды в час. Вам дается время в часах, и вам нужно
вернуть количество литров, которые Игорь выпьет, с округлением до наименьшего значения.

time1 = 3 --> litres = 1
time2 = 6.7 --> litres = 3
time3 = 11.8 --> litres = 5
"""
my_list_hours = [3, 6.7, 11.8]
my_list_result = []


def litres(kilometres):
    result = kilometres * 0.5
    return result


def append_to_list(us_list):
    for i in us_list:
        i = int(litres(i))
        my_list_result.append(i)
    return my_list_result


append_to_list(my_list_hours)
print(my_list_result)
