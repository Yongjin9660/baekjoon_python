# 나이순 정렬
import sys
N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    x, y = sys.stdin.readline().split()
    x = int(x)
    arr.append((x, y))
arr.sort(key=lambda x : (x[0]))

for x, y in arr:
    print(x, y)