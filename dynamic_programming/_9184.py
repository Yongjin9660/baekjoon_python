# 신나는 함수 실행
import sys

def www(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return www(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]
    
    if a < b < c:
        dp[a][b][c] = www(a, b, c-1) + www(a, b-1, c-1) - www(a, b-1, c)
        return dp[a][b][c]

    dp[a][b][c] = www(a-1, b, c) + www(a-1, b-1, c) + www(a-1, b, c-1) - www(a-1, b-1, c-1)
    return dp[a][b][c]
    

dp = [[[0] * (21) for _ in range(21)] for _ in range(21)]
dp[0][0][0] = 1

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {www(a, b, c)}')