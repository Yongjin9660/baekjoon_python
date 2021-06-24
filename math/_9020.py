# 골드바흐의 추측
import sys
isPrime = [False, False] + [True] * 10000
primes = []

for i in range(2, 10001):
    if isPrime[i] == True:
        primes.append(i)
        for j in range(2 * i, 10001, i):
            isPrime[j] = False

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    answer = [0, 0]
    for i in range(n // 2, 1, -1):
        if i in primes and (n - i) in primes:
            if i < n - i:
                answer[0] = i
                answer[1] = n - i
            else:
                answer[0] = n - i
                answer[1] = i
            break
    print(answer[0], answer[1])