import sys
M = int(sys.stdin.readline())
s = set()
for _ in range(M):
    temp = list(sys.stdin.readline().split())
    if temp[0] == 'add':
        s.add(int(temp[1]))
    elif temp[0] == 'remove':
        if int(temp[1]) in s:
            s.remove(int(temp[1]))
    elif temp[0] == 'check':
        if int(temp[1]) in s:
            print(1)
        else:
            print(0)
    elif temp[0] == 'toggle':
        if int(temp[1]) in s:
            s.remove(int(temp[1]))
        else:
            s.add(int(temp[1]))
    elif temp[0] == 'all':
        s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif temp[0] == 'empty':
        s.clear()