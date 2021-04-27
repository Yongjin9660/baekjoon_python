# 요세푸스 문제0

N, K = map(int, input().split())

arr = []

for i in range(1, N+1):
    arr.append(i)

i = 0
print("<", end='')

while True:
    if len(arr) == 1:
        print(arr[0], end=">")
        print()
        break
    i += K
    if i > len(arr):
        i = i % len(arr)
        if i == 0:
            i += len(arr)
    i -= 1
    print(arr.pop(i), end=", ")
