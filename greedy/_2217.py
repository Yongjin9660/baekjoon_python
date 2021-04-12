#  로프

import sys
N = int(sys.stdin.readline().strip())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().strip()))
arr.sort(reverse=True)

W = arr[0]
cnt = 1

for i in range(1, N):
    cnt += 1
    temp_W = arr[i] * cnt
    if temp_W > W:
        W = temp_W

print(W)