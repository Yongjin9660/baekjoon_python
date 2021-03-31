A = int(input())
B = int(input())
C = int(input())

result = A*B*C
arr = list(str(result))

for i in range(0,10):
    print(arr.count(str(i)))
