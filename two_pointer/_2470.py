# 두 용액
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

left = 0
right = N - 1
value = arr[left] + arr[right]

al = left
ar = right
while left < right:
    temp = arr[left] + arr[right]
    if abs(temp) < abs(value):
        value = temp
        al = left
        ar = right
        if value == 0:
            break
    if temp < 0:
        left += 1
    else:
        right -= 1

print(arr[al], arr[ar])