# 네 번째 점
dic_x = dict()
dic_y = dict()
for _ in range(3):
    x, y = map(int, input().split())
    if x in dic_x:
        dic_x[x] += 1
    else:
        dic_x[x] = 1
    if y in dic_y:
        dic_y[y] += 1
    else:
        dic_y[y] = 1

for i in dic_x:
    if dic_x[i] == 1:
        x = i
for i in dic_y:
    if dic_y[i] == 1:
        y = i
print(x,y)