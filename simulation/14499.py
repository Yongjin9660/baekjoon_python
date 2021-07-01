# 주사위 굴리기
N, M, y, x, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
command_list = list(map(int, input().split()))
dice = [[-1,0,-1],[0,0,0],[-1,0,-1],[-1,0,-1]]


for command in command_list:
    if command == 1:
        x += 1
        if x >= M:
            x -= 1
            continue
        dice[1][0], dice[1][1], dice[1][2] = dice[1][2], dice[1][0], dice[1][1]
        dice[1][0], dice[3][1] = dice[3][1], dice[1][0]
        if graph[y][x] == 0:
            graph[y][x] = dice[3][1]
        else:
            dice[3][1] = graph[y][x]
            graph[y][x] = 0
    elif command == 2:
        x -= 1
        if x < 0:
            x += 1
            continue
        dice[1][0], dice[1][1], dice[1][2] = dice[1][1], dice[1][2], dice[1][0]
        dice[1][2], dice[3][1] = dice[3][1], dice[1][2]
        if graph[y][x] == 0:
            graph[y][x] = dice[3][1]
        else:
            dice[3][1] = graph[y][x]
            graph[y][x] = 0
    elif command == 3:
        y -= 1
        if y < 0:
            y += 1
            continue
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
        if graph[y][x] == 0:
            graph[y][x] = dice[3][1]
        else:
            dice[3][1] = graph[y][x]
            graph[y][x] = 0
    elif command == 4:
        y += 1
        if y >= N:
            y -= 1
            continue
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
        if graph[y][x] == 0:
            graph[y][x] = dice[3][1]
        else:
            dice[3][1] = graph[y][x]
            graph[y][x] = 0
    print(dice[1][1])