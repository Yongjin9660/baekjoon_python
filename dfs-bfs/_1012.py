# 유기농 배추
from collections import deque

def bfs(y, x):
    graph[y][x] = 0
    deq = deque([(y, x)])
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if check(ny, nx) and graph[ny][nx] == 1:
                deq.append((ny, nx))
                graph[ny][nx] = 0

def check(y, x):
    if y >= 0 and x >= 0 and y < N and x < M:
        return True

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                cnt += 1
                bfs(y, x)
    print(cnt)     
