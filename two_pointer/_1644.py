# 소수의 연속합

N = int(input())
cnt = 0

n = 4000000
a = [False, False] + [True]*(n-1)
primes = []

for i in range(2, n):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n, i):
            a[j] = False

if N in primes:
    cnt += 1

left = 0
right = 1
temp_sum = primes[0] + primes[1]

while True:
    if N < 5:
        break
    if temp_sum == N:
        cnt += 1
        left += 1
        right = left + 1
        temp_sum = primes[left] + primes[right]
    elif temp_sum > N:
        left += 1
        right = left + 1
        temp_sum = primes[left] + primes[right]
        if temp_sum > N:
            break
    elif temp_sum < N:
        right += 1
        temp_sum += primes[right]
    
print(cnt)
