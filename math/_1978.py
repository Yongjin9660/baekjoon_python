# 소수 찾기
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

N = int(input().rstrip())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if isPrime(i) == True:
        cnt += 1
print(cnt)