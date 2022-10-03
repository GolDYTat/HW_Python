import random
from random import randint

len = int(input('Введите количество элементов списка: '))
a = []
for i in range(len):
    i = randint(-10, 10)
    a.append(i)
print('Список =>', a)

b = []
if len % 2 == 0:
    for i in range(int(len / 2)):
        b.append(a[i] * a[-i-1])
else: 
    for i in range(int(len / 2)):
        b.append(a[i] * a[-i-1]) 
    b.append(a[int((len - 1) / 2)] ** 2)      
print(b)


