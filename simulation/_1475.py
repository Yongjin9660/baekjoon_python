arr = list(map(int, input()))
print(arr)
dic = dict()
for i in arr:
    if i == 9:
        i = 6
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
if 6 in dic:
    if dic[6] % 2 == 0:
        dic[6] = dic[6] // 2
    else:
        dic[6] = dic[6] // 2 + 1
print(max(list(dic.values())))