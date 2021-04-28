# 좌표 압축

import sys
N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = list(sorted(set(arr)))
dic = {}
for i in range(len(arr2)):
    dic[arr2[i]] = i
for i in arr:
    print(dic[i], end = " ")