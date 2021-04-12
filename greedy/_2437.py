# 저울
import sys

N = int(sys.stdin.readline().strip())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
num = 1
for i in range(N):
    if num < arr[i]:
        break
    num += arr[i]

print(num)