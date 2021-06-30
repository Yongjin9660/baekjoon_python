E, S, M = map(int, input().split())

e, s, m = 1, 1, 1
result = 1
while True:
    if E == e and S == s and M == m:
        print(result)
        break
    e,s,m,result = e+1,s+1,m+1,result+1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1