# 피보나치 함수
import sys

T = int(sys.stdin.readline().rstrip())
dp = [(0, 0)] * 41
dp[0] = (1, 0)
dp[1] = (0, 1)

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    for i in range(0, n + 1):
        if dp[i] != (0, 0):
            continue
        dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

    print(dp[n][0], dp[n][1])