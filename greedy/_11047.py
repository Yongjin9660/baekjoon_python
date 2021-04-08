# 동전 0

n, k = map(int, input().split())

arr = []

for _ in range(n):
    temp = int(input())
    arr.append(temp)

cnt = 0

for i in range(n - 1, -1, -1):
    if k // arr[i] > 0:
        cnt += (k // arr[i])
        k = k % arr[i]
        if k == 0:
            break

print(cnt)