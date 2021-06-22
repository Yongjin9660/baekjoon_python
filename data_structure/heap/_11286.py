import sys, heapq

n = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(n):
    t = int(sys.stdin.readline().rstrip())
    if t == 0:
        if len(heap) == 0:
            print(0)
        else:
            a, b = heapq.heappop(heap)
            print(b)
    else:
        heapq.heappush(heap, (abs(t), t))
