n = int(input())
total = 2*n-1
blank = n-1
for i in range(1, n + 1):
    print(' ' * blank + '*' * (2*i-1))
    blank -= 1
blank = 1
for i in range(total - 2, -1, -2):
    print(' ' * blank + '*' * i)
    blank += 1
    