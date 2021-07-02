# 적록색약
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
visited = [[False] * N for _ in range(N)]
dy = [1,-1,0,0]
dx = [0,0,1,-1]
answer_1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            current = graph[i][j]
            q = deque([(i, j)])
            answer_1 += 1
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < N and 0 <= nx < N:
                        if graph[ny][nx] == current and visited[ny][nx] == False:
                            q.append((ny, nx))
                            visited[ny][nx] = True

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

answer_2 = 0
visited_2 = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited_2[i][j] == False:
            current = graph[i][j]
            q = deque([(i, j)])
            answer_2 += 1
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < N and 0 <= nx < N:
                        if graph[ny][nx] == current and visited_2[ny][nx] == False:
                            q.append((ny, nx))
                            visited_2[ny][nx] = True

print(answer_1, answer_2)