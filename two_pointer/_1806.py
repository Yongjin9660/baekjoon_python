# 부분합

import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
result = 0
temp_sum = 0

while True:
    if right < N and arr[right] >= S:
        result = 1
        break
    if temp_sum >= S:
        if result == 0:
            result = right - left
        else:
            result = min(result, right - left)
        temp_sum -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        temp_sum += arr[right]
        right += 1

print(result)