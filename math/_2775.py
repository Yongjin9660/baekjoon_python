# 부녀회장이 될테야
import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    arr = [[0] * (n + 1) for _ in range(k+1)]
    for i in range(1, n + 1):
        arr[0][i] = i
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            arr[i][j] = sum(arr[i-1][:j + 1])
    print(arr[k][n])