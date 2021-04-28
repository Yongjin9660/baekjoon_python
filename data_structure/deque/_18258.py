# 큐 2
import sys
from collections import deque

N = int(sys.stdin.readline().strip())

deq = deque()

for _ in range(N):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        deq.append(s[1])
    elif s[0] == 'pop':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(deq))
    elif s[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)