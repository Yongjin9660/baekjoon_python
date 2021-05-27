# 영화감독 숌

check_str = "666"

N = int(input())

number = 666
cnt = 0
while True:
    if check_str in str(number):
        cnt += 1
        if cnt == N:
            break
    number += 1

print(number)