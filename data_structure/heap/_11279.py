import heapq
import sys

heap = []
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    temp = int(sys.stdin.readline().rstrip())
    if temp == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -temp)