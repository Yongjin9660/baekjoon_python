s = input()

cur = s[0]
cnt = 0

for i in range(1, len(s)):
    if cur != s[i]:
        cnt += 1
        cur = s[i]

if cnt %2 == 0:
    print(cnt // 2)
else:
    print(cnt // 2 + 1)