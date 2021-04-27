# 군형잡힌 세상

import sys

while True:
    input_str = sys.stdin.readline().rstrip()
    if input_str == '.':
        break
    stack = []
    result = True

    for x in input_str:
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ')':
            if len(stack) == 0:
                result = False
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                result = False
                break
        elif x == ']':
            if len(stack) == 0:
                result = False
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                result = False
                break

    if len(stack) != 0:
        result = False
    if result == True:
        print('yes')
    else:
        print('no')