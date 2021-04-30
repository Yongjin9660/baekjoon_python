# 미로 탐색

from collections import deque

def bfs(y, x):
    deq = deque()
    deq.append((y, x))
    dist[y][x] = 1
    check[y][x] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while deq:
        yy, xx = deq.popleft()
        for i in range(4):
            ny = yy + dy[i]
            nx = xx + dx[i]
            if nx >= 0 and ny >= 0 and nx < M and ny < N:
                if check[ny][nx] == False and map[ny][nx] == "1":
                    deq.append((ny, nx))
                    dist[ny][nx] = dist[yy][xx] + 1
                    check[ny][nx] = True


N, M = map(int, input().split())
map = []
for _ in range(N):
    map.append(list(input()))
check = [[False] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]

bfs(0, 0)
print(dist[N-1][M-1])