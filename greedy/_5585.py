# 거스름돈
import sys
N = int(sys.stdin.readline().strip())

N = 1000 - N

arr = [500, 100, 50, 10, 5, 1]
cnt = 0
i = 0
while N != 0:
    if N // arr[i] >= 1:
        temp = N // arr[i]
        cnt += temp
        N = N - arr[i] * temp 
    i += 1


print(cnt) 