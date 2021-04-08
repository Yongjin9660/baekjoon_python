# 잃어버린 괄호

str = input().split('-')

temp = []

for x in str:
    s = x.split('+')
    temp_sum = 0
    for i in s:
        temp_sum += int(i)
    temp.append(temp_sum)

result = temp[0]
for i in range(1, len(temp)):
    result -= temp[i]

print(result)