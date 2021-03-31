s = input()

arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj' , 's=', 'z=']

for x in arr:
    s = s.replace(x, 'Q')

print(len(s))