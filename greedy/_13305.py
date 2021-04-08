# 주유소

N = int(input())

distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

min = prices[0]
sum = 0

for i in range(N-1):
    if min > prices[i]:
        min = prices[i]
    sum += (min * distances[i])

print(sum)