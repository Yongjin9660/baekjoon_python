# 집합의 표현

import sys
sys.setrecursionlimit(1000000)
n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]

def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    aa = find(a)
    bb = find(b)

    if aa < bb:
        parent[bb] = aa
    else:
        parent[aa] = bb

for _ in range(m):
    oper, a, b = map(int, sys.stdin.readline().split())
    if oper == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)