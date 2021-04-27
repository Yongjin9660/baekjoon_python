# AC
import sys
from collections import deque

def printArray(arr):
    print("[", end="")
    for i in range(len(arr)):
        print(arr[i], end="")
        if i != len(arr) - 1:
            print(",", end="")    
    print("]")

T = int(sys.stdin.readline().strip())

for _ in range(T):
    command = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())

    str = sys.stdin.readline().rstrip()
    if len(str) ==2:
        if 'D' in command:
            print("error")
        else:
            print("[]")
    else:
        error = False
        isReverse = False
        if ',' in str:
            str = deque(list(map(int, str[1:-1].split(','))))
        else:
            str = deque([int(str[1:-1])])
        for x in command:
            if x == 'R':
                if isReverse:
                    isReverse = False
                else:
                    isReverse = True
            else:
                if len(str) > 0:
                    if isReverse == True:
                        str.pop()
                    else:
                        str.popleft()
                else:
                    error = True
                    break
        if error == True:
            print("error")
        else:
            if isReverse == True:
                str.reverse()
                printArray(list(str))
            else:
                printArray(list(str))