# 입국심사
import sys

n, m = map(int, sys.stdin.readline().split())

times = []
for _ in range(n):
    times.append(int(sys.stdin.readline().rstrip()))

start = 1
end = max(times) * m

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for time in times:
        cnt += mid // time
        if cnt >= m:
            break
    if cnt >= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)