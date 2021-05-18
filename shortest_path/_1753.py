# 최단경로
import sys
import heapq

INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())


distance = [INF] * (V + 1)
graph = [[] for i in range(V + 1)]

for _ in range(E):
    u, v ,w = map(int, sys.stdin.readline().split())
    # (다음 노드, 거리)
    graph[u].append((v, w))


def dijkstra(start):
    min_heap = []
    distance[start] = 0
    # (거리, 노드)로 삽입
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        dist, node = heapq.heappop(min_heap)
        if distance[node] < dist:
            continue
        
        for i in graph[node]:
            temp_dist = i[1] + dist
            if temp_dist < distance[i[0]]:
                distance[i[0]] = temp_dist
                heapq.heappush(min_heap, (temp_dist, i[0]))
        

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])