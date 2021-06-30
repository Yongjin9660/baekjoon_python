n = int(input())
total = 2 * n - 1
for i in range(1, n+1):
    star = 2 * i - 1
    blank = (total - star) // 2
    print(' ' * blank + '*'*star)