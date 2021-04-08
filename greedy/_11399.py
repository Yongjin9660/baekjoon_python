# ATM

N = int(input())

list = list(map(int, input().split()))

# print(list)
list.sort()

sum = 0

for x in list:
    sum += (x*N)
    N -= 1

print(sum)