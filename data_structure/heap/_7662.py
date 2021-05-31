# 이중우선순위 큐
import sys
import heapq

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    visited = [False] * 1000001
    min_heap = []
    max_heap = []
    k = int(sys.stdin.readline().rstrip())
    for i in range(k):
        oper, number = sys.stdin.readline().split()

        if oper == 'I':
            number = int(number)
            heapq.heappush(min_heap, (number, i))
            heapq.heappush(max_heap, (-number, i))
            visited[i] = True
        else:
            if number == '1':
                while max_heap and visited[max_heap[0][1]] == False:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and visited[min_heap[0][1]] == False:
                    heapq.heappop(min_heap)
                if len(min_heap) > 0:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
                    
    while max_heap and visited[max_heap[0][1]] == False:
        heapq.heappop(max_heap)
    while min_heap and visited[min_heap[0][1]] == False:
        heapq.heappop(min_heap)
        
    if max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")