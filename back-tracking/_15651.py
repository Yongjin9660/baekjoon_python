# N과 M (3)
n, m = map(int, input().split())

result = []
def dfs(start):
    if len(result) == m:
        for x in result:
            print(x, end = " ")
        print()
        return
    
    for i in range(1, n + 1):
        result.append(i)
        dfs(i)
        result.pop()

dfs(1)