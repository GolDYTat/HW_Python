import random
from random import randint

len = int(input('Введите число: '))
a = []
for i in range(len):
    a.append(randint(-len, len))
print('Исходный список =>', a)

f = open(file.txt)