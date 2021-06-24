# 터렛
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    if x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
        continue
    dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if (r1 + r2) == dis or abs(r1 - r2) == dis:
        print(1)
    elif r1 + r2 < dis or abs(r1 - r2) > dis:
        print(0)
    else:
        print(2)