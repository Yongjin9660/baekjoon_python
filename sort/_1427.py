# 소트인사이드
import sys
N = list(sys.stdin.readline().rstrip())

N.sort(reverse=True)
for i in range(len(N)):
    print(N[i], end="")