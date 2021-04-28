# 두수의 합

import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
arr.sort()

count = 0
left = 0
right = n - 1

while left < right:
    if arr[right] >= x:
        right -= 1
        continue
    temp = arr[left] + arr[right]
    if temp == x:
        count += 1
        left += 1
        right -= 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(count)