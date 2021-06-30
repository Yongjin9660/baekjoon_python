# 2007년
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
x, y = map(int, input().split())
sum = y
for i in range(x):
    sum += days[i]
temp = sum % 7
if temp == 1:
    print('MON')
elif temp == 2:
    print('TUE')
elif temp == 3:
    print('WED')
elif temp == 4:
    print('THU')
elif temp == 5:
    print('FRI')
elif temp == 6:
    print('SAT')
elif temp == 0:
    print('SUN')