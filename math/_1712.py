# 손익분기점

A ,B, C = map(int, input().split())

if C <= B:
    print(-1)
else:
    cnt = A // (C - B)
    print(cnt + 1)