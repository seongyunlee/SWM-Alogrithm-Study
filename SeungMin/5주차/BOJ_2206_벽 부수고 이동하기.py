import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    temp = list(str(sys.stdin.readline().rstrip()))
    graph.append(list(map(int, temp)))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

q = deque()
q.append([0, 0, 0])
visited[0][0][0] = 1

while q:
    x, y, w = q.popleft()

    if x == n - 1 and y == m - 1:
        print(visited[x][y][w])
        exit()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                visited[nx][ny][w] = visited[x][y][w] + 1
                q.append([nx, ny, w])

            elif graph[nx][ny] == 1 and w == 0:
                visited[nx][ny][w + 1] = visited[x][y][w] + 1
                q.append([nx, ny, w + 1])

print(-1)
