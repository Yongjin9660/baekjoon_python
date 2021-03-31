C = int(input())

for _ in range(C):
    arr = list(map(int, input().split()))
    num = arr[0]
    s = sum(arr) - num
    average = s / num
    result = 0
    for i in range(1, num + 1):
        if arr[i] > average:
            result += 1
    per = result/num*100
    print('%.3f' % per, end ="")
    print("%")
