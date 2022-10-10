a = list(input("Введите числа через пробел:\n").split())

b = []
for i in a:
    if i not in b:
        b.append(i)
print(f"Список из неповторяющихся элементов: {b}")

for i in b:
    for i in a:
        if i in a == i in b:
            continue
        else:
            b.remove(i)
print(f"Список из неповторяющихся элементов: {b}")
