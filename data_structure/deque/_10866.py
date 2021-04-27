# 덱

from collections import deque
import sys

N = int(sys.stdin.readline())
deq = deque()

for _ in range(N):
    arr = list(sys.stdin.readline().split())
    if arr[0] == "push_front":
        deq.appendleft(arr[1])
    elif arr[0] == "push_back":
        deq.append(arr[1])
    elif arr[0] == "pop_front":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif arr[0] == "pop_back":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif arr[0] == "size":
        print(len(deq))
    elif arr[0] == "empty":
        if deq:
            print(0)
        else:
            print(1)
    elif arr[0] == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    else:
        if deq:
            print(deq[-1])
        else:
            print(-1)