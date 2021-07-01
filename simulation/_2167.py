n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
k = int(input())
for _ in range(k):
    i,j,x,y = map(int, input().split())
    i,j,x,y = i-1,j-1,x-1,y-1
    sum = 0
    for q in range(i, x + 1):
        for w in range(j, y + 1):
            sum += graph[q][w]
    print(sum)