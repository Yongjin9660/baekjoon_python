arr = [0] * 10001

for i in range(1, 10001):
    sum = i
    sum += i % 10
    i = i // 10

    while i > 0:
        sum += i % 10
        i = i // 10
    
    if sum < 10001:
        arr[sum] = 1

for i in range(1, 10001):
    if arr[i] == 0:
        print(i)