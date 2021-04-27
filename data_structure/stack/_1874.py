# 스택 수열

import sys

n = int(sys.stdin.readline())

stack = []
check = True
result = []

count = 1
for i in range(n):
    num = int(sys.stdin.readline())
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        check = False

if check == True:
    for i in result:
        print(i)
else:
    print("NO")