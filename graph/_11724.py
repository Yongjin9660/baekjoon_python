# 연결 요소의 개수
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N+1)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True

cnt = 0
for i in range(1, N + 1):
    if visited[i] == False:
        bfs(i)
        cnt += 1
print(cnt)