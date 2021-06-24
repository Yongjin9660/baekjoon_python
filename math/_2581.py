# 소수
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a = int(input().rstrip())
b = int(input().rstrip())
sum = 0
isFirst = False
first_num = -1
for i in range(a, b + 1):
    if isPrime(i) == True:
        if isFirst == False:
            isFirst = True
            first_num = i
        sum += i
if isFirst == False:
    print(-1)
else:
    print(sum)
    print(first_num)