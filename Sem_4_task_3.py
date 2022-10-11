from random import randint

dict = {}

nums = ''.join(list(map(str, [randint(0, 9) for x in range(10)])))
print(nums)

for i in nums:
    if dict.get(i):
        dict[i] = dict.get(i) + 1
    else:
        dict[i] = 1

result = []
for i in dict:
    if dict[i] == 1:
        result.append(i)

print(result)