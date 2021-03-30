import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N, 0, -1):
    for j in range(1, N+1):
        if j>=i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
