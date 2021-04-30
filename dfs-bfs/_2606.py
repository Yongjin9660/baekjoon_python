# 바이러스
from collections import deque

def dfs(graph, visited, v):
    visited[v] = True
    global cnt
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(graph, visited, i)
            cnt += 1

def bfs(graph, visited, v):
    deq = deque([v])
    visited[v] = True
    global cnt
    while deq:
        temp = deq.popleft()
        for x in graph[temp]:
            if visited[x] == False:
                cnt += 1
                visited[x] = True
                deq.append(x)


N = int(input())
M = int(input())
cnt = 0
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs(graph, visited, 1)
bfs(graph, visited, 1)

print(cnt)