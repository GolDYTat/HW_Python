from encodings import utf_8

pathInputCompression = 'file_Sem_5_task_4_input_compression.txt'
pathInputExpansion = 'file_Sem_5_task_4_input_expansion.txt'
pathOutput = 'file_Sem_5_task_4_output.txt'

dataCompression = ''
dataExpansion = ''

def RLE_Compression(fileData):
    result = ''
    second = ''
    count = 1
    for i in fileData:
        if i != second:
            if second:
                result += str(count) + second
            count = 1
            second = i
        else:
            count += 1
    else:
        result += str(count) + second
        return result

def RLE_Expansion(fileData):
    result = '' 
    count = '' 
    for i in fileData:
        if i.isdigit():
            count += i
        else:
            result += i * int(count)
            count = ''
    return result

with open(pathInputCompression) as file:
    dataCompression = file.read()

with open(pathInputExpansion) as file:
    dataExpansion = file.read()

with open(pathOutput, 'w', encoding = 'utf_8') as file:
    file.write(f'Сжатие: {RLE_Compression(dataCompression)}\n')
    file.write(f'Восстановление: {RLE_Expansion(dataExpansion)}')