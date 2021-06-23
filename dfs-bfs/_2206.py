# 벽 부수고 이동하기
import sys
from collections import deque

INF = int(1e9)

def bfs(x, y):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    q = deque()
    visited[0][x][y] = 1
    q.append((0,x,y))

    while q:
        block, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아니고 방문한 적이 없다면
                if graph[nx][ny] == 0 and visited[block][nx][ny] == INF:
                    visited[block][nx][ny] = visited[block][x][y] + 1
                    q.append((block, nx, ny))
                # 벽이고 한번도 뚫은적 없고 벽이 뚫린 기록이 없다면
                elif graph[nx][ny] == 1 and block == 0 and visited[1][nx][ny] == INF:
                    visited[1][nx][ny] = visited[block][x][y] + 1
                    q.append((1, nx, ny))
    return min(visited[0][n-1][m-1], visited[1][n-1][m-1])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[[INF] * m for _ in range(n)] for _ in range(2)]

for _ in range(n):
    temp_list = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(temp_list)

dis = bfs(0, 0)
if dis == INF:
    print(-1)
else:
    print(dis)