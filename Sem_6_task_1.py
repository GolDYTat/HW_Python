import random
from random import randint

# len = int(input('Введите количество элементов списка: '))
# a = []
# for i in range(len):
#     i = randint(-10, 10)
#     a.append(i)
# print('Исходный список =>', a)
# random.shuffle(a)
# print('Перемешанный список =>',a)


len = int(input('Введите количество элементов списка: '))
a = [randint(-10, 10) for i in range(len)]
print('Исходный список =>', a)
random.shuffle(a)
print('Перемешанный список =>',a)