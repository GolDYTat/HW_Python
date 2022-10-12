from random import randint

def data(name):
    x = int(input(f"{name}, введите количество (от 1 до 28) конфет, которое возьмете: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def printBalance(name, k, count, value):
    print(f"{name} взял {k} конфет, теперь у него {count} конфет. На столе осталось {value} конфет.")

def bot():
    k = randint(1,29)
    return k

def playerVSplayer():
    player1 = input("Введите имя первого игрока: ")
    player2 = input("Введите имя второго игрока: ")
    value = 150
    flag = randint(0,2)
    if flag:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")
    count1 = 0 
    count2 = 0
    while value > 28:
        if flag:
            k = data(player1)
            count1 += k
            value -= k
            flag = False
            printBalance(player1, k, count1, value)
        else:
            k = data(player2)
            count2 += k
            value -= k
            flag = True
            printBalance(player2, k, count2, value)
    if flag:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")

def playerVSbot():
    player1 = input("Введите имя первого игрока: ")
    player2 = "Компьютер"
    value = 150
    flag = randint(0,2)
    if flag:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")
    count1 = 0 
    count2 = 0
    while value > 28:
        if flag:
            k = data(player1)
            count1 += k
            value -= k
            flag = False
            printBalance(player1, k, count1, value)
        else:
            k = bot()
            count2 += k
            value -= k
            flag = True
            printBalance(player2, k, count2, value)
    if flag:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")

version = int(input('\n Для игры против компьютера введите: 1 \n Для игры против другого игрока введите: 2 \n'))

if version == 1:
    playerVSbot()
elif version == 2:
    playerVSplayer()