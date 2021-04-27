# 프린터 큐
from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    deq = deque()
    for i in range(N):
        deq.append((i, arr[i]))
    arr.sort(reverse=True)
    result = 0
    while True:
        index, value = deq.popleft()
        if value == arr[0]:
            result += 1
            if index == M:
                print(result)
                break
            arr.pop(0)
        else:
            deq.append((index, value))