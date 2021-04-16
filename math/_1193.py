# 분수찾기

X = int(input())

if X == 1:
    print("1/1")
else:
    n = 1
    # 몇번째 줄인지 찾기
    while True:
        if n*(n + 1) // 2 < X and X <= (n + 1)*(n + 2) // 2:
            break
        n += 1

    s = n*(n + 1) // 2
    turn = X - s
    n += 1
    if n % 2 == 0:
        son = turn
        parent = n + 1 - turn
        print(f'{son}/{parent}')
    else:
        son = n + 1 - turn
        parent = turn
        print(f'{son}/{parent}')