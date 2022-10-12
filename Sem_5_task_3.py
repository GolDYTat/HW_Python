import sys, os
from random import randint

version = int(input('\n Для игры с ботом введите: 1 \n Для игры с игроком введите 2: \n'))

position = []
for i in range(1, 10):
    position.append(i)

gamer1 = 'Игрок 1'
gamer2 = 'Игрок 2'
moves = []
win = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

def winCond():
    sign = 'O'
    for i in win:
        if position[i[0]-1] == position[i[1]-1] == position[i[2]-1]:
            sys.exit(f"\n Игра окончена")
                      
def printBoard(position):
    print('-------------------')
    print(f'|{position[0]:^5}|{position[1]:^5}|{position[2]:^5}|')
    print('-------------------')
    print(f'|{position[3]:^5}|{position[4]:^5}|{position[5]:^5}|')
    print('-------------------')
    print(f'|{position[6]:^5}|{position[7]:^5}|{position[8]:^5}|')
    print('-------------------')

def playerVSplayer():
    sign = 'O'
    while True:
        os.system('cls||clear')
        while True:
            printBoard(position)
            index = int(input(f"\n Ходит {gamer2 if sign == 'X' else gamer1}: "))
            if index in moves:
                print('Эта клетка уже занята')
            else:
                if sign == 'O':
                    sign = 'X'
                else:
                    sign = "O"
                moves.append(index)
                position[index - 1] = sign
                winCond()
                break

def playerVSbot():
    os.system('cls||clear')
    while True:
        while True: 
            sign = 'X' 
            printBoard(position)
            indexBot = randint(1, 9)
            if indexBot in moves:
                indexBot = randint(1, 9)
            else:
                sign = 'X'    
            moves.append(indexBot)
            position[indexBot - 1] = sign
            winCond()
            break
        while True:
            sign = 'O' 
            printBoard(position)
            index = int(input(f"\n Ходит {gamer1}: "))
            if index in moves:
                print('Эта клетка уже занята')
            else:
                sign == 'O'
            moves.append(index)
            position[index - 1] = sign
            winCond()
            break

if version == 1:
    playerVSbot()
elif version == 2:
    playerVSplayer()