# 여행 가자

import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

def find(x):
    if x == parent[x]:
        return x
    p = find(parent[x])
    parent[x] = p
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, N + 1):
    temp_list = list(map(int, sys.stdin.readline().split()))
    for j in range(1, N + 1):
        if temp_list[j - 1] == 1:
            union(i, j)

order = list(map(int, sys.stdin.readline().split()))
result = set()
for i in order:
    result.add(find(i))

if len(result) == 1:
    print("YES")
else:
    print("NO")
