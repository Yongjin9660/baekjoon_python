# 통계학
import sys
N = int(sys.stdin.readline())
arr = []
dic = {}
sum = 0
for _ in range(N):
    temp = int(sys.stdin.readline())
    sum += temp
    arr.append(temp)

    if temp in dic.keys():
        dic[temp] += 1
    else:
        dic[temp] = 1

arr.sort()

dic = sorted(dic.items(), key=lambda x : (x[1], -x[0]), reverse=True)
average = int(round(sum/N, 0))

print(average)
print(arr[N//2])
if len(dic) > 1 and dic[0][1] == dic[1][1]:
    print(dic[1][0])
else:
    print(dic[0][0])
print(arr[N-1]-arr[0])