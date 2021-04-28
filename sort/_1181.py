# 단어 정렬
import sys
N = int(sys.stdin.readline())

s = set()
for _ in range(N):
    s.add(sys.stdin.readline().rstrip())

arr = list(s)
new_arr = []
for s in arr:
    new_arr.append((len(s), s))
new_arr.sort(key=lambda x:(x[0],x[1]))

for x,y in new_arr:
    print(y)