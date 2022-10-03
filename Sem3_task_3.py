import random
import math

len = int(input('Введите количество элементов списка: '))
a = []
for i in range(len):
    i = random.uniform(10, 20)
    a.append(round(i, 2))
print('Список =>', a)

b = []
for i in range(len):
    n = math.modf(a[i])
    b.append((round(n[0], 2)) * 100)

max = b[i]
min = b[i]
for i in range(len):
    if b[i] > max:
        max = b[i] 
    if b[i] < min:
        min = b[i]

print(f'Разница между максимальным и минимальным значением дробной части элементов: {(max - min)/100}')
