n = int(input())
total = 2 * n

for i in range(1, n+1):
    blank = total - (i * 2)
    print('*'*i + ' ' * blank + '*'*i)

for i in range(n-1, 0, -1):
    blank = total - i * 2
    print('*'*i + ' ' * blank + '*'*i)
