# 소수 구하기
M, N = map(int, input().split())

isPrime = [False, False] + [True] * N
primes = []
for i in range(2, N + 1):
    if isPrime[i]:
        primes.append(i)
        for j in range(i * 2, N + 1, i):
            isPrime[j] = False
for i in primes:
    if i >= M:
        print(i)