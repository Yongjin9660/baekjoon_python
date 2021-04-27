# 카드2
from collections import deque

N = int(input())
deq = deque()

for i in range(1, N + 1):
    deq.append(i)

while True:
    if len(deq) == 1:
        print(deq[0])
        break
    deq.popleft()
    deq.append(deq.popleft())