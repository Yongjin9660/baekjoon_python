# 토마토
from collections import deque

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cnt = -1
    while deq:
        cnt += 1
        for _ in range(len(deq)):
            yy, xx = deq.popleft()
            for i in range(4):
                ny = yy + dy[i]
                nx = xx + dx[i]
                if (0 <= nx < M) and (0 <= ny < N) and arr[ny][nx] == 0:
                    arr[ny][nx] = 1
                    deq.append([ny, nx])
    
    for a in arr:
        if 0 in a:
            return -1
    return cnt


M, N = map(int, input().split())

arr = []
deq = deque()

for y in range(N):
    row = list(map(int, input().split()))
    for x in range(M):
        if row[x] == 1:
            deq.append([y, x])
    arr.append(row)

print(bfs())