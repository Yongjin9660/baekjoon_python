# 전자레인지

import sys

T = int(sys.stdin.readline().strip())

ten = 0
thirty = 0
six = 0

if T % 10 != 0:
    print(-1)
else:
    ten = T // 10
    if ten // 30 >= 1:
        thirty = ten // 30
        ten = ten % 30
    if ten // 6 >= 1:
        six = ten // 6
        ten = ten % 6
    print(thirty, six, ten)