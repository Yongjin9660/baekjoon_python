# 뱀
def check(y, x):
    if 1 <= y <= N and 1 <= x <= N:
        return True
    return False

from collections import deque
N = int(input())
K = int(input())
apples = []
for _ in range(K):
    y, x = map(int, input().split())
    apples.append((y,x))

change = deque()
L = int(input())
for _ in range(L):
    t, alpha = input().split()
    change.append((int(t), alpha))

snake = deque()
snake.append((1,1))
head_y, head_x = 1, 1
d = 0
time = 0
while True:
    time += 1
    if d == 0:
        head_x += 1
    elif d == 1:
        head_y += 1
    elif d == 2:
        head_x -= 1
    elif d == 3:
        head_y -= 1

    if check(head_y, head_x) == False or (head_y, head_x) in snake:
        break
    if (head_y, head_x) in apples:
        snake.appendleft((head_y, head_x))
        apples.pop(apples.index((head_y, head_x)))
    else:
        for i in range(len(snake)-1,0,-1):
            snake[i] = snake[i-1]
        snake.popleft()
        snake.appendleft((head_y, head_x))
    if len(change) > 0 and change[0][0] == time:
        if change[0][1] == 'D':
            if d == 0:
                d = 1
            elif d == 1:
                d = 2
            elif d == 2:
                d = 3
            elif d == 3:
                d = 0
        elif change[0][1] == 'L':
            if d == 0:
                d = 3
            elif d == 1:
                d = 0
            elif d == 2:
                d = 1
            elif d == 3:
                d = 2
        change.popleft()
print(time)