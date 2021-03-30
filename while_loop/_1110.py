N = int(input())

if N < 10:
    temp = N * 11
else:
    t1 = (N % 10) + (N // 10)
    temp = (N % 10)*10 + (t1 % 10)

result = 1

while temp != N:
    t1 = (temp % 10) + (temp // 10)
    temp = (temp % 10)*10 + (t1 % 10)
    result += 1

print(result)