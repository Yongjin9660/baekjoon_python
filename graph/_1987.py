# 알파벳
import sys
R, C = map(int, sys.stdin.readline().split())
graph = []
for _ in range(R):
    graph.append(list(sys.stdin.readline().rstrip()))

dy = [1,-1,0,0]
dx = [0,0,1,-1]

visited = [[False] * C for _ in range(R)]

def dfs(y, x, cnt):
    global answer
    if cnt == 26:
        answer = 26
        return
    answer = max(answer, cnt)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C:
            if alpha[ord(graph[ny][nx]) - 65] == False:
                alpha[ord(graph[ny][nx]) - 65] = True
                dfs(ny, nx, cnt + 1)
                alpha[ord(graph[ny][nx]) - 65] = False
    
alpha = [False] * 26
alpha[ord(graph[0][0]) - 65] = True
answer = 1
dfs(0, 0, 1)
print(answer)