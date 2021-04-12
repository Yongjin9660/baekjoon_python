# 센서

N = int(input())
K = int(input())

arr = list(map(int, input().split()))
arr.sort()

if N == 1:
    print(0)
else:
    temp = []

    for i in range(N-1):
        temp.append(arr[i+1] - arr[i])

    temp.sort()

    for _ in range(K-1):
        temp.pop()

    print(sum(temp))