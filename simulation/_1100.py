graph = []
for _ in range(8):
    graph.append(list(input()))
cnt = 0
for i in range(0,8,2):
    for j in range(0,8,2):
        if graph[i][j] == 'F':
            cnt += 1
for i in range(1,8,2):
    for j in range(1,8,2):
        if graph[i][j] == 'F':
            cnt += 1
print(cnt)