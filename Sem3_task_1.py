import random
from random import randint

len = int(input('Введите количество элементов списка: '))
a = []
for i in range(len):
    i = randint(-10, 10)
    a.append(i)
print('Список =>', a)

summ = 0
for i in range(1, len, 2):
    summ += a[i]
        
print('Сумма элементов на нечетных позициях равна:', summ)