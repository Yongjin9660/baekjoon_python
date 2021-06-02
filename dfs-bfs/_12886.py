# 돌 그룹
import sys
from collections import deque

stones = list(map(int, sys.stdin.readline().split()))
visited = dict()
total = sum(stones)
if total % 3 != 0:
    print(0)
else:
    check = False
    q = deque()
    q.append(stones)
    visited[tuple(stones)] = True
    while q:
        a, b, c = q.popleft()
        if a == b == c:
            check = True
            break
        for x, y in ((a,b), (a, c), (b, c)):
            if x == y:
                continue
            elif x < y:
                y -= x
                x += x
            elif y < x:
                x -= y
                y += y
            z = total - x - y
            temp_list = [x, y, z]
            temp_list.sort()
            temp_tuple = (temp_list[0], temp_list[1], temp_list[2])
            if temp_tuple not in visited:
                visited[temp_tuple] = True
                q.append(temp_tuple)
    if check:
        print(1)
    else:
        print(0)