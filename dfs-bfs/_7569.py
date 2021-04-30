# 토마토

import sys
from collections import deque

def bfs():
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    cnt = -1

    while deq:
        cnt += 1
        for _ in range(len(deq)):
            zz, yy, xx = deq.popleft()
            for i in range(6):
                nx = xx + dx[i]
                ny = yy + dy[i]
                nz = zz + dz[i]
                if check(nz, ny, nx) and box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = 1
                    deq.append((nz, ny, nx))

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 0:
                    return -1
    return cnt
    

def check(z, y, x):
    if (0 <= x < M) and (0 <= y < N) and (0 <= z < H):
        return True


M, N, H = map(int, sys.stdin.readline().split())

box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

deq = deque()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                deq.append((z, y, x))

print(bfs())