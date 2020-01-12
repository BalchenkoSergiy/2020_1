"""
1. Дан список words. Составьте из него список слов-палиндромов. Попробуйте это сделать двумя способами: произвольное решение и решение в одну строчку кода.
2. Дан список my_str со строками, часть из которых являются палиндромами. Составьте новый список строк-палиндромов.
"""
print('************************** Task 1 *********************************************')
#1
words = ['мадам', 'топот', 'test', 'madam', 'word']
res_list = [i for i in words if i[:].lower() == i[::-1].lower()]
print(res_list)

print('************************** Task 2 *********************************************')
#2
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']

res_list = [i for i in my_str if (i[:].lower()).replace(' ', '') == (i[::-1].lower()).replace(' ', '')]
print(res_list)