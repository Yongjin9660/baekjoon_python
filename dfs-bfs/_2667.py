# 단지번호 붙이기
def check(x, y):
    if x >= 0 and y >= 0 and x < N and y < N:
        return True
    else:
        return False

def dfs(i, j):
    global cnt
    cnt += 1
    graph[i][j] = "0"

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for z in range(4):
        nx = i + dx[z]
        ny = j + dy[z]
        if check(nx, ny) and graph[nx][ny] == "1":
            dfs(nx, ny)


N = int(input())

graph = []
result = []

for _ in range(N):
    graph.append(list(input()))

for i in range(N):
    for j in range(N):
        if graph[i][j] == "1":
            cnt = 0
            dfs(i, j)
            result.append(cnt)

result.sort()
print(len(result))
for x in result:
    print(x)