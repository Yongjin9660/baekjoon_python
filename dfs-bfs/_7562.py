# 나이트의 이동
import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,1,-1]
for _ in range(T):
    q = deque()
    I = int(sys.stdin.readline().rstrip())
    a = [[0] * I for _ in range(I)]
    x0, y0 = map(int, sys.stdin.readline().split())
    x, y = map(int, sys.stdin.readline().split())
    q.append((x0, y0))
    a[x0][y0] = 1
    while q:
        temp_x, temp_y = q.popleft()
        if temp_x == x and temp_y == y:
            print(a[temp_x][temp_y]-1)
            break
        for i in range(8):
            nx = temp_x + dx[i]
            ny = temp_y + dy[i]
            if 0 <= nx < I and 0 <= ny < I:
                if a[nx][ny] == 0:
                    q.append((nx, ny))
                    a[nx][ny] = a[temp_x][temp_y] + 1