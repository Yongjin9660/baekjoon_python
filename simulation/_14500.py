# 테트로미노
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

tetromino = [
    [(0,0), (0,1), (1,0), (1,1)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,2), (0,1)], 
    [(0,0), (1,0), (2,0), (1,1)], 
    [(1,0), (0,1), (1,1), (2,1)], 
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

def cal(x, y):
    global result
    for i in range(19):
        temp_result = 0
        for j in range(4):
            try:
                temp_x = x + tetromino[i][j][0]
                temp_y = y + tetromino[i][j][1]
                temp_result += graph[temp_x][temp_y]
            except IndexError:
                continue
        result = max(result, temp_result)


result = 0
for i in range(n):
    for j in range(m):
        cal(i, j)
print(result)