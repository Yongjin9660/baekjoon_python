n1, n2 = input().split()

n1_reverse = n1[::-1]
n2_reverse = n2[::-1]

if int(n1_reverse) > int(n2_reverse):
    print(n1_reverse)
else:
    print(n2_reverse)