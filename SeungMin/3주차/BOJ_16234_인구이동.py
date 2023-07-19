import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().rstrip().split())
land = []
for i in range(N):
    land.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    connect = deque()
    people, count = 0, 0
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        connect.append((x, y))
        count += 1
        people += land[x][y]
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if 0 <= nextX < N and 0 <= nextY < N:
                if visited[nextX][nextY] == 0:
                    diff = abs(land[x][y] - land[nextX][nextY])
                    if L <= diff <= R:
                        visited[nextX][nextY] = count
                        q.append((nextX, nextY))
    while connect:
        x, y = connect.popleft()
        land[x][y] = (people // count)

    if count == 1:
        return 0
    return 1

answer = 0
while True:
    q = deque()
    break_cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                q.append((i, j))
                break_cnt += bfs(i, j)
    if break_cnt == 0:
        break
    else:
        answer += 1

print(answer)
