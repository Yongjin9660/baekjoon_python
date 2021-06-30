n = int(input())

for i in range(n, -1, -1):
    star = '*' * i
    blank = ' ' * (n - i)
    s = blank + star
    print(s)