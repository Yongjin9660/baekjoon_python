# DFS와 BFS
from collections import deque

def dfs(graph, visited, v):
    print(v, end = " ")
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, visited, i)

def bfs(graph, visited, v):
    deq = deque([v])
    visited[v] = True
    print(v, end = " ")

    while deq:
        temp = deq.popleft()
        for i in graph[temp]:
            if visited[i] == False:
                deq.append(i)
                visited[i] = True
                print(i, end = " ")

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

for i in range(N + 1):
    graph[i].sort()

dfs(graph, visited_dfs, V)
print()
bfs(graph, visited_bfs, V)
print()