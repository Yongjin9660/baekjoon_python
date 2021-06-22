T = int(input().rstrip())
for _ in range(T):
    H, W, N = map(int, input().split())
    room = N // H + 1
    h = N % H
    if h == 0:
        h = H
        room -= 1
    if room < 10:
        print(str(h) + '0' + str(room))
    else:
        print(str(h) + str(room))