# 벌집

N = int(input())

n = 1
while True:
    temp = 3*n*n - 3*n + 1
    if temp >= N:
        print(n)
        break
    else:
        n += 1