# 덩치
N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

for i in range(N):
    a, b = arr[i]
    rank = 1
    for j in range(N):
        if i == j:
            continue
        temp_a, temp_b = arr[j]
        if a < temp_a and b < temp_b:
            rank += 1
    print(rank, end = " ")
print()
