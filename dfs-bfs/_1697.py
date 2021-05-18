# 숨바꼭질
from collections import deque

def bfs():
    while deq:
        for _ in range(len(deq)):
            x, cnt = deq.popleft()

            if visited[x] == False:
                visited[x] = True
                if x == K:
                    return cnt
                cnt += 1
                if x * 2 <= 100000:
                    deq.append((x * 2, cnt))
                if x + 1 <= 100000:
                    deq.append((x + 1, cnt))
                if x - 1 >= 0:
                    deq.append((x - 1, cnt))

N, K = map(int, input().split())
deq = deque()
deq.append((N, 0))
visited = [False] * 100001
print(bfs())