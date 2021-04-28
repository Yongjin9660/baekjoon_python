# 사이클 게임
import sys

def find(x):
    if x == parent[x]:
        return x
    temp = find(parent[x])
    parent[x] = temp
    return temp

def union(x, y):
    xx = find(x)
    yy = find(y)

    if xx == yy:
        return
    if xx < yy:
        parent[yy] = xx
    else:
        parent[xx] = yy

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n)]
check = False
count = 0

for _ in range(m):
    count += 1
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        check = True
        break
    union(a, b)

if check == True:
    print(count)
else:
    print(0)