num = input('Введите любое число: ')

sum = 0
for i in num:
    if i != '.':
        sum += int(i)
   
print('Сумма чисел в данном числе равна:', sum)