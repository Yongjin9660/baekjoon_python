s = "...!@BaT#*..y.abcdefghijklm"

se = set()
for i in s:
    if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
        continue
    else:
        se.add(i)
for i in se:
    print(i)
    s = s.replace(i, "")

print(s)