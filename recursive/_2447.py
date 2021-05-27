# 별 찍기 - 10
def star(y, x, n):
    if n == 1:
        graph[y][x] = '*'
        return
    div = int(n / 3)
    star(x, y, div)
    star(x + div, y, div)
    star(x + div + div, y, div)
    star(x, y + div, div)
    star(x + div + div, y + div, div)
    star(x, y + div + div, div)
    star(x + div, y + div + div, div)
    star(x + div + div, y + div + div, div)

n = int(input())
graph = [[' '] * (n) for _ in range(n)]
star(0, 0, n)
for i in range(n):
    print(''.join(graph[i]))