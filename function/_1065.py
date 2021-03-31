import sys

def hansoo(a):
    if a <= 99:
        return True
    elif a == 1000:
        return False
    
    arr = []

    while a > 0:
        temp = a % 10
        a = a // 10
        arr.append(temp)

    #arr.sort()

    if (arr[1]-arr[0]) == (arr[2]-arr[1]):
        return True
    else:
        return False
    

N = int(sys.stdin.readline().rstrip())

result = 0

for i in range(1, N + 1):
    if hansoo(i) == True:
        result += 1

print(result)