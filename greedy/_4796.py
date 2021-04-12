# 캠핑
import sys

case = 1
while True:
    L, P, V = map(int, sys.stdin.readline().strip().split())
    if L == 0:
        break
    result = 0
    
    n = V // P
    res = V % P

    result += (L * n)
    if res > L:
        result += L
    else:
        result += res

    print(f'Case {case}: {result}')
    case += 1