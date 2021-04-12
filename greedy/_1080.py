# 행렬
import sys

def flip(n, m):
    for i in range(n, n + 3):
        for j in range(m, m + 3):
            A[i][j] = 1 - A[i][j]

N, M = map(int, sys.stdin.readline().strip().split())

A = []
B = []

for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().strip())))
for _ in range(N):
    B.append(list(map(int, sys.stdin.readline().strip())))

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B [i][j]:
            flip(i, j)
            cnt += 1

check = True
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            check = False
            break

if check == True:
    print(cnt)
else:
    print(-1)