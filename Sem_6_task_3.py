import random
from random import randint

# len = int(input('Введите число: '))
# a = []
# for i in range(len):
#     i = randint(-len, len)
#     a.append(i)
# print('Исходный список =>', a)

# f = open('file.txt')
# b = []
# for i in f:
#     b.append(i)

# mult = a[int(b[0])] * a[int(b[1])]
# print(f'Произведение элементов с индексами, которые хранятся в file.txt равняется:   {mult}')


len = int(input('Введите число: '))
a = [randint(-len, len) for i in range(len)]
print('Исходный список =>', a)
f = open('file.txt')
b = [i for i in f]
def mult(a):
    return a[int(b[0])] * a[int(b[1])]
print(f'Произведение элементов с индексами, которые хранятся в file.txt равняется:   {mult(a)}')