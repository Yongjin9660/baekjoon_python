from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

queue = deque([x])

while queue:
	now_node = queue.popleft()
	for next_node in graph[now_node]:
		if distance[next_node] == -1:
			distance[next_node] = distance[now_node] + 1
			queue.append(next_node)

check = False

for i in range(n+1):
	if distance[i] == k:
		check = True
		print(i)

if check == False:
	print(-1)
