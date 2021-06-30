# 음계
arr = list(map(int, input().split()))
ascen = [1,2,3,4,5,6,7,8]
decen = [8,7,6,5,4,3,2,1]
if arr == ascen:
    print("ascending")
elif arr == decen:
    print("descending")
else:
    print("mixed")