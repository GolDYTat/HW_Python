count = int(input('Введите количество чисел последовательности: '))

a = []
c = 0
sum = 0
for i in range(0, count):
    i += 1
    c = (1 + 1 / i) ** i
    sum += c
    a.append(round(c, 3))
print('Последовательность =>', a)
print('Сумма чисел в последовательности:', round(sum, 3))