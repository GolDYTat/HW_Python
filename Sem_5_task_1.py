path = 'file_Sem_5_task_1.txt'

text = input('Введите букву (все слова с данной буквой будут удалены): ')

data = ''

with open(path, encoding = 'utf_8') as file:
    data = file.read()
print(data)
data = data.split()

result = []

for w in data:
    if text not in w:
        result.append(w)

print(result)