# 회전하는 큐

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
target = list(map(int, sys.stdin.readline().split()))

deq = deque()
for i in range(1, N + 1):
    deq.append(i)

result = 0
for i in range(M):
    idx = deq.index(target[i])
    if idx == 0:
        deq.popleft()
        continue
    temp = len(deq) // 2
    if temp >= idx:
        result += (idx)
        for _ in range(idx):
            deq.append(deq.popleft())
        deq.popleft()
    else:
        result += (len(deq) - idx)
        l = len(deq)
        for _ in range(l - idx):
            deq.appendleft(deq.pop())
        deq.popleft()

print(result)