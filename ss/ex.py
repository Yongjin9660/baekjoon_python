def rotate(arr, n, start_y, start_x, end_y, end_x):
    while n > 1:
        upper = []
        lower = []
        left = []
        right = []
        idx = start_x
        for i in range(n):
            upper.append(arr[start_y][idx])
            idx += 1

        idx = start_x
        for i in range(n):
            lower.append(arr[end_y][idx])
            idx += 1

        idx = start_y
        for _ in range(n):
            left.append(arr[idx][start_x])
            idx += 1

        idx = start_y
        for _ in range(n):
            right.append(arr[idx][end_x])
            idx += 1

        idx = start_y
        for i in range(n):
            arr[idx][end_x] = upper[i]
            idx += 1
        idx = start_x
        for i in range(n-1, -1, -1):
            arr[end_y][idx] = right[i]
            idx += 1
        idx = start_y
        for i in range(n):
            arr[idx][start_x] = lower[i]
            idx += 1
        idx = start_x
        for i in range(n-1, -1, -1):
            arr[start_y][idx] = left[i]
            idx += 1

        start_x += 1
        start_y += 1
        end_x -= 1
        end_y -= 1
        n = n // 2

arr = [[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]]

rotate(arr, 8, 0, 0, 7, 7)
for i in range(8):
    for j in range(8):
        print(arr[i][j], end=" ")
    print()