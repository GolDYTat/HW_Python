from math import pi

d =  int(input("Введите количество знаков после запятой для числа Pi: "))

p = round(pi, d)
print('Pi равно:', p)