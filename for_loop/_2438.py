import sys

N = int(sys.stdin.readline().rstrip())

for i in range(1, N + 1):
    for _ in range(i):
        print("*", end="")
    print("")