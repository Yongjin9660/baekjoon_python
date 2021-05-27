# 치킨 배달
import sys
from itertools import combinations

def dis(graph, pos_list):
    temp_graph = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp_graph[i][j] = graph[i][j]

    for pos in pos_list:
        y, x = pos
        temp_graph[y][x] = 0

    home_pos = []
    chi_pos = []
    for i in range(N):
        for j in range(N):
            if temp_graph[i][j] == 2:
                chi_pos.append((j, i))
            elif temp_graph[i][j] == 1:
                home_pos.append((j, i))
    result = 0
    for home in home_pos:
        home_y, home_x = home
        temp_dis = int(1e9)
        for chi in chi_pos:
            chi_y, chi_x = chi
            t = abs(chi_y - home_y) + abs(chi_x - home_x)
            temp_dis = min(temp_dis, t)
        result += temp_dis

    return result

N, M = map(int, sys.stdin.readline().split())
graph = []

chi_num = 0
chi_pos = []

for i in range(0, N):
    li = list(map(int, sys.stdin.readline().split()))
    for j in range(0, N):
        if li[j] == 2:
            chi_pos.append((i, j))
            chi_num += 1
    graph.append(li)

closed = chi_num - M
per_list = list(combinations(chi_pos, closed))

result = int(1e9)

for pos_list in per_list:
    result = min(result, dis(graph, pos_list))
print(result)