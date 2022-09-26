x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))

a = not(x or y or z)
b = (not x) and (not y) and (not z)
if a == b:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')