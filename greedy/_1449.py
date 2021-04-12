# 수리공 항승

N, L = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

start = arr[0] - 0.5
end = start + L
cnt = 1
for i in range(1, N):
    if start <= arr[i] - 0.5 and arr[i] + 0.5 <= end:
        continue
    else:
        cnt += 1
        start = arr[i] - 0.5
        end = start + L
print(cnt)