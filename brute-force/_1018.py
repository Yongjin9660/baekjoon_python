# 체스판 다시 칠하기

def paint(graph):
    # 맨 왼쪽 위가 W
    cnt = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    if graph[i][j] == 'B':
                        cnt += 1
                else:
                    if graph[i][j] == 'W':
                        cnt += 1
            else:
                if j % 2 == 0:
                    if graph[i][j] == 'W':
                        cnt += 1
                else:
                    if graph[i][j] == 'B':
                        cnt += 1
    temp_cnt = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    if graph[i][j] == 'W':
                        temp_cnt += 1
                else:
                    if graph[i][j] == 'B':
                        temp_cnt += 1
            else:
                if j % 2 == 0:
                    if graph[i][j] == 'B':
                        temp_cnt += 1
                else:
                    if graph[i][j] == 'W':
                        temp_cnt += 1
    cnt = min(temp_cnt, cnt)
    return cnt

import copy
N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(input()))
y = 0
x = 0
result = int(1e9)
cnt = 0
temp_graph = [[0] * 8 for _ in range(8)]
while True:
    temp_y = y
    temp_x = x

    for i in range(8):
        for j in range(8):
            temp_graph[i][j] = graph[temp_y][temp_x]
            temp_x += 1
        temp_y += 1
        temp_x = x
    result = min(result, paint(temp_graph))
    x += 1
    if x + 8 > M:
        x = 0
        y += 1
        if y + 8 > N:
            break
print(result)
