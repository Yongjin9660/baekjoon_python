# 하노이 탑 이동 순서
def hanoi(n, a, b, c):
    global sum
    if n == 1:
        moves.append((a, c))
        return
    hanoi(n-1, a, c, b)
    moves.append((a, c))
    hanoi(n-1, b, a, c)

moves = []
n = int(input())
hanoi(n, 1, 2, 3)

print(len(moves))
for move in moves:
    a, b = move
    print(a, b)