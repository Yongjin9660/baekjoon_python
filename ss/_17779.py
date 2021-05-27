# 게리멘더링 2
import sys
N = int(sys.stdin.readline().rstrip())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

result = int(1e9)
total = 36
for x in range(N):
    for y in range(N):
        if x == y == 0 or x == y == N - 1:
            continue
        d1 = 1
        d2 = 1
        while True:
            left = (x, y)
            upper = (x + d1, y - d1)
            bottom = (x + d2, y + d2)
            right = (x + d1 + d2, y + d1 - d2)

            temp_1 = 0
            for i in range(x):
                for j in range(y):
                    temp_1 += graph[j][i]
            for 


            d2 += 1
            if x + d2 >= N or y + d2 >= N:
                d1 += 1
                d2 = 1
                if x + d1 >= N or y - d1 < 0:
                    break 
