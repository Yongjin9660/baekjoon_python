str = input()

arr = [-1] * 26

for i in range(len(str)):
    alpha = ord(str[i]) - 97
    if arr[alpha] == -1:
        arr[alpha] = i

for i in arr:
    print(i, end = " ")