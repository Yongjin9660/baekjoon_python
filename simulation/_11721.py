s = input()
idx = 0
while True:
    temp = s[idx:idx+10]
    if temp == '':
        break
    else:
        print(temp)
        idx += 10
