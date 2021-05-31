# N과 M (2)
n, m = map(int, input().split())

visited = [False] * (n + 1)
result = []

def dfs(start):
    if len(result) == m:
        for x in result:
            print(x, end = " ")
        print()

    for i in range(start, n + 1):
        if visited[i] == False:
            result.append(i)
            visited[i] = True
            dfs(i + 1)
            visited[i] = False
            result.pop()
dfs(1)