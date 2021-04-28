# 수 정렬하기
import sys
N = int(sys.stdin.readline())
arr=[]

for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()
for i in range(N):
    print(arr[i]) 