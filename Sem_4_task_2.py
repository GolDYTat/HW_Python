num = int(input("Введите число: "))

list = []
i = 2 
while i <= num:
    if num % i == 0:
        list.append(i)
        num //= i
    else:
        i += 1

print('Список простых множителей для данного числа:', list)