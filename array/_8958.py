import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    str = input()
    se = 0
    sum = 0
    for i in str:
        if i == 'O':
            se += 1
            sum += se
        else:
            se = 0
    print(sum)
