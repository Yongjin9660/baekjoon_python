n = int(input())

arr = list(map(int, input().split()))

M = max(arr)

for i in range(n):
    arr[i] = arr[i]/M*100

print(sum(arr) / n)