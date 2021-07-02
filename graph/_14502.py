# 연구소
import sys
from collections import deque
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
graph = []
viruses = []
possibles = []
for i in range(N):
    temp_list = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if temp_list[j] == 2:
            viruses.append((i, j))
        elif temp_list[j] == 0:
            possibles.append((i, j))
    graph.append(temp_list)

def bfs():
    global result
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for y, x in viruses:
        q = deque([(y,x)])
        while q:
            cur_y, cur_x = q.popleft()
            for i in range(4):
                ny = cur_y + dy[i]
                nx = cur_x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    cnt += 1
    result = min(result, cnt)

result = int(1e9)
for arr in list(combinations(possibles, 3)):
    for i, j in arr:
        graph[i][j] = 1
    bfs()
    for i, j in arr:
        graph[i][j] = 0
walls = M * N - len(viruses)- len(possibles)
print(M * N - len(viruses) - result - walls - 3)