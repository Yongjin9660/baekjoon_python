# 설탕 배달
import sys
N = int(sys.stdin.readline().strip())

n_five = N // 5
res = N % 5

if N == 3:
    print(1)
elif N == 4:
    print(-1)
else:
    while True:
        if n_five == 0 and res % 3 != 0:
            print(-1)
            break
        if res % 3 == 0:
            print(n_five + (res//3))
            break
        else:
            n_five -= 1
            res += 5
            continue