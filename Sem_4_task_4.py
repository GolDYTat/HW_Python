import random

k = int(input("Введите степень: "))

def write_file(name, ect):
    with open(name, 'w') as data:
        data.write(ect)

def rnd():
    return random.randint(0, 100)

def index(k):
    list = [rnd() for i in range(k + 1)]
    return list
 
def ecuation(indx):
    list = indx[::-1]
    wst = ''
    if len(list) < 1:
        wst = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wst += f'{list[i]}x^{len(list)-i-1}'
                if list[i+1] != 0:
                    wst += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                wst += f'{list[i]}x'
                if list[i+1] != 0:
                    wst += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                wst += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                wst += ' = 0'
    return wst

write_file('file_Sem_4_task_4.txt', ecuation(index(k)))