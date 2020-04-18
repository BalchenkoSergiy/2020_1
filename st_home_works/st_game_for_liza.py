# **********************************************************************************************************************
# **********************************************************************************************************************
# *****Game for Elizabeth'
import random


def first_number():
    result = random.randint(0, 10)
    return result


def second_number():
    result = random.randint(0, 10)
    return result


def make_numb():
    numOne = first_number()
    numTwo = second_number()
    numDict = {'One': numOne, 'Two':numTwo}
    return numDict


def choise_oper(numDict):
    if numDict['One'] > numDict['Two']:
        operator = '-'
    elif numDict['One'] < numDict['Two']:
        operator = '+'
    return operator





def gener_task(num_dict, oper):
    if oper == '+':
        result = num_dict['One'] + num_dict['Two']
    elif oper == '-':
        result = num_dict['One'] - num_dict['Two']
    return result

print('Привіт користувач! Мене звати Комп\'ютер')
print('Давай пограємо в гру. Я буду задавати тобі приклади')
print('Спробуй розв\'язати їх!')


def main():
    num_dict = make_numb()
    oper = choise_oper(num_dict)

    print('Скільки буде: ', str(num_dict['One']) + choise_oper(num_dict) + str(num_dict['Two']))
    result = gener_task(num_dict, oper)

    while True:

        answer = int(input('Будь- ласка введи свою відповідь: '))
        if answer == result:
            print(f'Ура!!! Молодець')
            print('А тепер новий приклад!')
            break
        else:
            print('Не вірно, спробуй порахувати ще раз!!!')


main()