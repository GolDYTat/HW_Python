a = int(input('Введите номер четверти: '))

if a > 4 or a < 1:
    print('Введите корректные данные')
elif a == 1:
    print('В данной четверти X - положительное, Y - положительное')
elif a == 2:
    print('В данной четверти X - отрицательное, Y - положительное')
elif a == 3:
    print('В данной четверти X - отрицательное, Y - отрицательное')
elif a == 4:
    print('В данной четверти X - положительное, Y - отрицательное')