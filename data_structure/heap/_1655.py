import sys, heapq

n = int(sys.stdin.readline().rstrip())
left = []
right = []
for _ in range(n):
    t = int(sys.stdin.readline().rstrip())
    if len(left) == len(right):
        heapq.heappush(left, -t)
    else:
        heapq.heappush(right, t)
    
    if len(right) > 0 and -left[0] > right[0]:
        temp_right = heapq.heappop(right)
        temp_left = -heapq.heappop(left)
        heapq.heappush(right, temp_left)
        heapq.heappush(left, -temp_right)
    print(-left[0])