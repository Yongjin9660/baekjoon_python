# 영역 구하기
import sys
from collections import deque
M, N, K = map(int, sys.stdin.readline().split())
graph = [[1] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 0

visited = [[False] * N for _ in range(M)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            q = deque([(i,j)])
            cnt = 1
            visited[i][j] = True
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 1 and visited[ny][nx] == False:
                        q.append((ny, nx))
                        cnt += 1
                        visited[ny][nx] = True
            answer.append(cnt)
answer.sort()
print(len(answer))
for i in answer:
    print(i, end = " ")