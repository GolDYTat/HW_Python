num = int(input('Введите целое число: '))

a = []
factorial = 1
for i in range(num):
    i += 1
    factorial *= i
    a.append(factorial)
print(f'Произведение чисел от 1 до',num, '=>', a)