# 친구 네트워크

import sys

def find(f):
    if f == parent[f]:
        return f
    a = find(parent[f])
    parent[f] = a
    return a

def union(f1, f2):
    a = find(f1)
    b = find(f2)
    if a == b:
        print(count[a])
        return 
    if a < b:
        parent[b] = a
        count[a] += count[b]
        print(count[a])
    else:
        parent[a] = b
        count[b] += count[a]
        print(count[b])


T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    parent = {}
    count = {}

    for _ in range(n):
        f1, f2 = sys.stdin.readline().split()

        if f1 not in parent:
            parent[f1] = f1
            count[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            count[f2] = 1
        union(f1, f2)