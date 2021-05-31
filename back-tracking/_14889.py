# 스타트와 링크
from itertools import combinations
    
N = int(input())
person = [i for i in range(N)]
board = []

for i in range(N):
    board.append(list(map(int, input().split())))

combi_list = list(combinations(person, N//2))

min_value = int(1e9)

for start in combi_list:
    link = []
    for i in range(N):
        if i not in start:
            link.append(i)

    score_start = 0
    score_link = 0

    each_start = list(combinations(start, 2))
    each_link = list(combinations(link, 2))
    for each in each_start:
        a, b = each
        score_start += board[a-1][b-1] + board[b-1][a-1]
    for each in each_link:
        a, b = each
        score_link += board[a-1][b-1] + board[b-1][a-1]
    temp = abs(score_start - score_link)
    min_value = min(temp, min_value)

print(min_value)

