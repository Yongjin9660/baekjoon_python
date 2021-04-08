# 회의실 배정

N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort()
arr.sort(key=lambda x:x[1])

cnt = 0
time = 0
for x in arr:
    a, b = x
    if a >= time:
        cnt += 1
        time = b

print(cnt)