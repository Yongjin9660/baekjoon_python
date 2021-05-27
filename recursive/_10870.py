# 피보나치 수 5
def fibo(n):
    if n == 1 or n == 0:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))