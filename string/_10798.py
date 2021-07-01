arr = []
max_len = -1
for _ in range(5):
    temp = list(input())
    max_len = max(max_len, len(temp))
    arr.append(temp)

for j in range(max_len):
    for i in range(5):
        if len(arr[i]) <= j:
            continue
        print(arr[i][j], end='')