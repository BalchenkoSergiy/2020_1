from my_easy_calc.classes import *


task = {'x': x(), 'y': y()}
obj_class = Calc(task['x'], task['y'])

#print(task['x'], type(task['x'])) # 5 <class 'int'>
#print(task['y'], type(task['y'])) # 10 <class 'int'>
#print(f'x = {obj_class.x}') # x = 5
#print(f'y = {obj_class.y}') # y = 10
#print(f'{obj_class.x} + {obj_class.y} = {obj_class.plus()}') # 5 + 10 = 15
#print(f'{obj_class.x} - {obj_class.y} = {obj_class.minus()}') # 5 - 10 = -5
#print(f'{obj_class.x} / {obj_class.y} = {obj_class.divided()}') # 5 / 10 = 0.5
#print(f'{obj_class.x} * {obj_class.y} = {obj_class.multiply()}') # 5 * 10 = 50