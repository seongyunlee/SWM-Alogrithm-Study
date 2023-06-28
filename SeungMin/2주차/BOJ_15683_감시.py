import sys
import copy

N, M = map(int, sys.stdin.readline().rstrip().split())
office = []
cctv = []
answer = N * M
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def watch(x, y, dir, tempoffice):
    for i in dir:
        nextX = x
        nextY = y
        while True:
            nextX += dx[i]
            nextY += dy[i]
            if 0 <= nextX < M and 0 <= nextY < N and tempoffice[nextY][nextX] != 6:
                if tempoffice[nextY][nextX] == 0:
                    tempoffice[nextY][nextX] = '#'
            else:
                break


def dfs(num, office):
    global answer
    temparr = copy.deepcopy(office)

    dir1 = [[0], [1], [2], [3]]
    dir2 = [[0, 1], [2, 3]]
    dir3 = [[0, 2], [0, 3], [1, 2], [1, 3]]
    dir4 = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
    dir5 = [[0, 1, 2, 3]]
    if num == len(cctv):
        temp = 0
        for i in temparr:
            temp += i.count(0)
        answer = min(answer, temp)

        return

    x, y, cctvnum = cctv[num]
    if cctvnum == 1:
        for i in dir1:
            watch(x, y, i, temparr)
            dfs(num + 1, temparr)
            temparr = copy.deepcopy(office)

    elif cctvnum == 2:
        for i in dir2:
            watch(x, y, i, temparr)
            dfs(num + 1, temparr)
            temparr = copy.deepcopy(office)

    elif cctvnum == 3:
        for i in dir3:
            watch(x, y, i, temparr)
            dfs(num + 1, temparr)
            temparr = copy.deepcopy(office)

    elif cctvnum == 4:
        for i in dir4:
            watch(x, y, i, temparr)
            dfs(num + 1, temparr)
            temparr = copy.deepcopy(office)

    elif cctvnum == 5:
        for i in dir5:
            watch(x, y, i, temparr)
            dfs(num + 1, temparr)
            temparr = copy.deepcopy(office)

for i in range(N):
    office.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    for j in range(M):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv.append([j, i, office[i][j]])

dfs(0, office)
print(answer)
