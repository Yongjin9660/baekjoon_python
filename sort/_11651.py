# 좌표 정렬하기 2
import sys
N = int(sys.stdin.readline())
arr = [] 
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key = lambda x : (x[1], x[0]))
for i in range(N):
    print(arr[i][0], arr[i][1])