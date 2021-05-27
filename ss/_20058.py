# 파이어스톰
import sys
from collections import deque

def check(arr):
    temp_arr = [[-1] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            temp_arr[i][j] = arr[i][j]

    for y in range(size):
        for x in range(size):
            if temp_arr[y][x] != 0:
                cnt = 0
                if y - 1 >= 0:
                    if temp_arr[y - 1][x] > 0:
                        cnt += 1
                if y + 1 < size:
                    if temp_arr[y + 1][x] > 0:
                        cnt += 1
                if x - 1 >= 0:
                    if temp_arr[y][x - 1] > 0:
                        cnt += 1
                if x + 1 < size:
                    if temp_arr[y][x + 1] > 0:
                        cnt += 1
                if cnt < 3:
                    arr[y][x] -= 1

def rotate(arr, n, start_y, start_x, end_y, end_x):
    while n > 1:
        upper = []
        lower = []
        left = []
        right = []
        idx = start_x
        for i in range(n):
            upper.append(arr[start_y][idx])
            idx += 1

        idx = start_x
        for i in range(n):
            lower.append(arr[end_y][idx])
            idx += 1

        idx = start_y
        for _ in range(n):
            left.append(arr[idx][start_x])
            idx += 1

        idx = start_y
        for _ in range(n):
            right.append(arr[idx][end_x])
            idx += 1

        idx = start_y
        for i in range(n):
            arr[idx][end_x] = upper[i]
            idx += 1
        idx = start_x
        for i in range(n-1, -1, -1):
            arr[end_y][idx] = right[i]
            idx += 1
        idx = start_y
        for i in range(n):
            arr[idx][start_x] = lower[i]
            idx += 1
        idx = start_x
        for i in range(n-1, -1, -1):
            arr[start_y][idx] = left[i]
            idx += 1

        start_x += 1
        start_y += 1
        end_x -= 1
        end_y -= 1
        n -= 2
    
N, Q = map(int, sys.stdin.readline().split())
size = 2 ** N
arr = []
for _ in range(size):
    arr.append(list(map(int, sys.stdin.readline().split())))

list_L = list(map(int, sys.stdin.readline().split()))

for l in list_L:
    temp_size = 2 ** l
    idx_y = 0
    idx_x = 0
    while True:
        rotate(arr, temp_size, idx_y, idx_x, idx_y + temp_size - 1, idx_x + temp_size -1)
        idx_x += temp_size
        if idx_x >= size:
            idx_x = 0
            idx_y += temp_size
            if idx_y >= size:
                break
    check(arr)

queue = deque()
visited = [[False] * size for _ in range(size)]
max_value = 0

dx=[1,-1,0,0]
dy=[0,0,1,-1]

for i in range(size):
    for j in range(size):
        if arr[i][j] > 0 and visited[i][j] == False:
            queue.append((i, j))
            visited[i][j] = True
            cnt = 1
            while queue:
                temp_y, temp_x = queue.popleft()
                for k in range(4):
                    yy = temp_y + dy[k]
                    xx = temp_x + dx[k]
                    if size > xx >= 0 and size > yy >= 0 and visited[yy][xx] == False and arr[yy][xx] > 0:
                        visited[yy][xx] = True
                        queue.append((yy, xx))
                        cnt += 1
            max_value = max(max_value, cnt)

sum = 0
for i in range(size):
    for j in range(size):
        sum += arr[i][j]
print(sum)
print(max_value)