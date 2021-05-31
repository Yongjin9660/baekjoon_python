# N과 M (1)
n, m = map(int, input().split())

result = []
visited = [False] * (n + 1)

def dfs(depth, n):
    if depth == m + 1:
        for x in result:
            print(x, end = " ")
        print()
        return
    for num in range(1, n + 1):
        if visited[num] == False:
            visited[num] = True
            result.append(num)
            dfs(depth + 1, n)
            visited[num] = False
            result.pop()

dfs(1, n)