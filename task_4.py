x1 = float(input('Введите X для первой точки: '))
y1 = float(input('Введите Y для первой точки: '))
x2 = float(input('Введите X для второй точки: '))
y2 = float(input('Введите Y для второй точки: '))

distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
print(round(distance ** 0.5, 2))