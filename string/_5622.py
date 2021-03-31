arr = ['ABC','DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

s = input()

sum = 0

for x in s:
    for i in range(len(arr)):
        if x in arr[i]:
            sum = sum + i + 3

print(sum)