num = int(input('Введите целое число: '))

n1 = 1
n2 = 1
list = []
for i in range(num):
    list.append(n1)
    n1, n2 = n2, n1 + n2
n1, n2 = 0, 1
for i in range (num + 1):
    list.insert(0, n1)
    n1, n2 = n2, n1 - n2

print(list)
