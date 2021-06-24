# 소인수분해
N = int(input())

def primeNumber(k):
    for i in range(2, k + 1):
        if k % i == 0:
            return i

while N != 1:
    prime = primeNumber(N)
    print(prime)
    N = N // prime      