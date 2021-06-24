# 베르트랑 공준
isPrime = [False, False] + [True] * 250000
primes = []
for i in range(2, 250000):
    if isPrime[i]:
        primes.append(i)
        for j in range(i * 2, 250000, i):
            isPrime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for prime in primes:
        if n < prime <= 2*n:
            cnt += 1
        elif prime > 2 * n:
            break
    print(cnt)