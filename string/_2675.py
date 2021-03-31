T = int(input())

for _ in range(T):
    num, s = input().split()
    result = ""
    for i in range(len(s)):
        result += s[i] * int(num)
    print(result)