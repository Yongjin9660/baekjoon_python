n = int(input())

s = ''
for i in range(n):
    if i % 2 == 0:
        s += '*'
    else:
        s += ' '
s += '\n'
for i in range(n):
    if i % 2 == 0:
        s += ' '
    else:
        s += '*'
s += '\n'
s = s * n
print(s, end = '')