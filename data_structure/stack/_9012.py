# 괄호
import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    stack = []
    input_str = sys.stdin.readline().rstrip()
    result = True
    for x in input_str:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) == 0:
                result = False
                break
            if stack[-1] == '(':
                stack.pop()
                continue
            else:
                result = False
                break
    if stack:
        result = False
    if result == True:
        print("YES")
    else:
        print("NO")