# 안전 영역
import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
graph = []
max_height = -1
for _ in range(N):
    temp_list = list(map(int, sys.stdin.readline().split()))
    max_height = max(max_height, max(temp_list))
    graph.append(temp_list)
result = 1
def check(y,x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False

def bfs():
    global result
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0 and visited[i][j] == False:
                visited[i][j] = True
                q = deque()
                q.append((i, j))
                cnt += 1
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if check(ny, nx) == True and visited[ny][nx] == False and graph[ny][nx] != 0:
                            visited[ny][nx] = True
                            q.append((ny, nx))
    result = max(result, cnt)

for h in range(1, max_height):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == h:
                graph[i][j] = 0
    bfs()
print(result)