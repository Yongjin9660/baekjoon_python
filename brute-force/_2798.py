# 블랙잭
from itertools import combinations

N, M = map(int, input().split())

arr = list(map(int, input().split()))

combi_list = list(combinations(arr, 3))

result = -1
for combi in combi_list:
    a, b, c = combi
    temp_sum = a + b + c
    if temp_sum <= M:
        result = max(result, temp_sum)

print(result)