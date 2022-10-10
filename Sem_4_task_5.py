import random
from Sem_4_task_4 import write_file, rnd, index, ecuation

def sq_indx(kf):
    if 'x^' in kf:
        i = kf.find('^')
        num = int(kf[i+1:])
    elif ('x' in kf) and ('^' not in kf):
        num = 1
    else:
        num = -1
    return num

def k_indx(kf):
    if 'x' in kf:
        i = kf.find('x')
        num = int(kf[:i])
    return num

def calc_indx(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_indx(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 
    ii = l - 1 
    while ii >= 0:
        if sq_indx(st[ii]) != -1 and sq_indx(st[ii]) == i:
            lst.append(k_indx(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst
    
k1 = int(input("Введите пераую степень: "))
k2 = int(input("Введите вторую степень: "))
kf1 = index(k1)
kf2 = index(k2)
write_file("file_Sem_4_task_5_1.txt", ecuation(kf1))
write_file("file_Sem_4_task_5_2.txt", ecuation(kf2))

with open('file_Sem_4_task_5_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file_Sem_4_task_5_2.txt', 'r') as data:
    st2 = data.readlines()
print("Первый многочлен", st1)
print("Второй многочлен", st2)
list1 = calc_indx(st1)
list2 = calc_indx(st2)
ll = len(list1)
if len(list1) > len(list2):
    ll = len(list2)
list_new = [list1[i] + list2[i] for i in range(ll)]
if len(list1) > len(list2):
    mm = len(list1)
    for i in range(ll,mm):
        list_new.append(list1[i])
else:
    mm = len(list2)
    for i in range(ll,mm):
        list_new.append(list2[i])
write_file("file_Sem_4_task_result.txt", ecuation(list_new))
with open('file_Sem_4_task_result.txt', 'r') as data:
    st3 = data.readlines()
print('Сумма сложения многочеленов:', st3)