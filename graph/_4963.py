# 섬의 개수
import sys
from collections import deque

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    def check(y, x):
        if 0 <= x < w  and 0 <= y < h:
            return True
        return False

    visited = [[False] * w for _ in range(h)]

    def bfs(i, j):
        dx = [-1,-1,-1,0,0,1,1,1]
        dy = [-1,0,1,-1,1,-1,0,1]
        q = deque()
        q.append((i, j))
        while q:
            y, x = q.popleft()
            for k in range(8):
                ny = y + dy[k]
                nx = x + dx[k]
                if check(ny, nx) == True:
                    if visited[ny][nx] == False and graph[ny][nx] == 1:
                        q.append((ny, nx))
                        visited[ny][nx] = True

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                bfs(i, j)
                cnt += 1
    print(cnt)
                