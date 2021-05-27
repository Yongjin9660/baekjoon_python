# 블랙잭
from itertools import combinations

N, M = map(int, input().split())

arr = list(map(int, input().split()))

combi_list = list(combinations(arr, 3))
print(combi_list)
