# 연산자 끼워넣기
import copy

temp_operator = []
def dfs_operator(idx):
    if len(temp_operator) == operator_cnt:
        temp = copy.deepcopy(temp_operator)
        operator_list.append(temp)
        return
    for i in range(operator_cnt):
        if visited_operator[i] == False:
            visited_operator[i] = True
            temp_operator.append(operators[i])
            dfs_operator(0)
            visited_operator[i] = False
            temp_operator.pop()

N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())

operator_cnt = plus + minus + multiple + divide

operators = []
for _ in range(plus):
    operators.append("+")
for _ in range(minus):
    operators.append("-")
for _ in range(multiple):
    operators.append("*")
for _ in range(divide):
    operators.append("/")

visited_operator = [False] * operator_cnt
operator_list = []

dfs_operator(0)

max_value = -int(1e9)
min_value = int(1e9)

for operators in operator_list:
    idx = 0
    temp_value = numbers[idx]
    for operator in operators:
        idx += 1
        if operator == '+':
                temp_value += numbers[idx]
        elif operator == '-':
            temp_value -= numbers[idx]
        elif operator == '*':
            temp_value *= numbers[idx]
        elif operator == '/':
            if temp_value > 0:
                temp_value = temp_value // numbers[idx]
            else:
                temp_value = -(temp_value)
                temp_value //= numbers[idx]
                temp_value = -(temp_value)

    max_value = max(max_value, temp_value)
    min_value = min(min_value, temp_value)

print(max_value)
print(min_value)