import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
maps = []
goal = []
lenarr = [[-1] * m for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue = []
    queue.append([x, y])
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nextX, nextY = x + dx[i], y + dy[i]
            if 0 <= nextX < n and 0 <= nextY < m and lenarr[nextX][nextY] == -1:
                if maps[nextX][nextY] == 0:
                    lenarr[nextX][nextY] = 0
                elif maps[nextX][nextY] == 1:
                    lenarr[nextX][nextY] = lenarr[x][y] + 1
                    queue.append([nextX, nextY])


for i in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            lenarr[i][j] = 0
            bfs(i, j)
            break

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            print(0, end = ' ')
        else:
            print(lenarr[i][j], end = ' ')
    print('')
