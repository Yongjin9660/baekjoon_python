# 로봇 청소기
def check(r, c):
    if 0 <= r < n and 0 <= c < m:
        return True
    else:
        return False

def isBlock(graph, r, c):
    cnt = 0
    if check(r+1, c) == False:
        cnt += 1
    else:
        if graph[r+1][c] != 0:
            cnt += 1
    if check(r, c+1) == False:
        cnt += 1
    else:
        if graph[r][c+1] != 0:
            cnt += 1
    if check(r-1, c) == False:
        cnt += 1
    else:
        if graph[r-1][c] != 0:
            cnt += 1
    if check(r, c-1) == False:
        cnt += 1
    else:
        if graph[r][c-1] != 0:
            cnt += 1
    if cnt == 4:
        return True
    else:
        return False

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
result = 0
temp = 2
while True:
    if graph[r][c] == 0:
        graph[r][c] = temp
        temp += 1
        result += 1
    if isBlock(graph, r, c) == True:
        if d == 0:
            if check(r+1, c) == False or graph[r+1][c] == 1:
                break
            r += 1
            continue
        elif d == 1:
            if check(r, c-1) == False or graph[r][c-1] == 1:
                break
            c -= 1
            continue
        elif d == 2:
            if check(r-1, c) == False or graph[r-1][c] == 1:
                break
            r -= 1
            continue
        elif d == 3:
            if check(r, c+1) == False or graph[r][c+1] == 1:
                break
            c += 1
            continue
    while True:
        if d == 0:
            d = 3
            if check(r, c-1) == True and graph[r][c-1] == 0:
                c -= 1
                break
        elif d == 1:
            d = 0
            if check(r-1, c) == True and graph[r-1][c] == 0:
                r -= 1
                break
        elif d == 2:
            d = 1
            if check(r, c+1) == True and graph[r][c+1] == 0:
                c += 1
                break
        elif d == 3:
            d = 2
            if check(r+1, c) == True and graph[r+1][c] == 0:
                r += 1
                break

print(result)