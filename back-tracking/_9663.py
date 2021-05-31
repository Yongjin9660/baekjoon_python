# N-Queen
import sys

def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i] - col[x]) == x - i:
            return False
    return True

def backTracking(x):
    global count
    if x == N:
        count += 1
        return 
    for i in range(N):
        col[x] = i
        if check(x):
            backTracking(x + 1)

N = int(sys.stdin.readline().rstrip())
col = [0] * N
count = 0
backTracking(0)
print(count)