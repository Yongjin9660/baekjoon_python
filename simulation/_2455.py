current = 0
max_value = 0
for _ in range(4):
    a, b = map(int, input().split())
    current += (b-a)
    max_value = max(max_value, current)
print(max_value)