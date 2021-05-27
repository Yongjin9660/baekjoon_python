# 분해합
N = int(input())
check = False
for i in range(N):
    temp_sum = i
    str_num = str(i)
    for j in range(len(str_num)):
        temp_sum += int(str_num[j])
    if temp_sum == N:
        check = True
        break
if check:
    print(i)
else:
    print(0)