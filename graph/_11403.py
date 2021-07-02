# 경로 찾기
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N)]
for i in range(N):
    temp_list = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if temp_list[j] == 1:
            graph[i].append(j)
visited = [[False] * N for _ in range(N)]
result = [[0] * N for _ in range(N)]

def bfs(i, v):
    q = deque([v])
    while q:
        temp_v = q.popleft()
        result[i][temp_v] = 1
        for k in graph[temp_v]:
            if visited[i][k] == False:
                visited[i][k] = True
                q.append(k)
                
for i in range(N):
    for v in graph[i]:
        if visited[i][v] == False:
            visited[i][v] = True
            bfs(i, v)
for i in range(N):
    for j in range(N):
        print(result[i][j], end = ' ')
    print()