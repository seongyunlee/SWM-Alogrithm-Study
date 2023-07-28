import copy
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
lab = []

for i in range(N):
    lab.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
virus = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.append([i, j])


def select_wall(start, count):
    global answer
    if count == 3:
        temp_lab = copy.deepcopy(lab)
        for num in range(len(virus)):
            x, y = virus[num]
            spread(x, y, temp_lab)
        safe_counts = sum(i.count(0) for i in temp_lab)
        answer = max(answer, safe_counts)
        return True
    else:
        for i in range(start, N * M):
            x = i // M
            y = i % M
            if lab[x][y] == 0:
                lab[x][y] = 1
                select_wall(i, count + 1)
                lab[x][y] = 0


def spread(x, y, temp_lab):
    if temp_lab[x][y] == 2:
        for i in range(4):
            nextx = x + dx[i]
            nexty = y + dy[i]

            if 0 <= nextx < N and 0 <= nexty < M:
                if temp_lab[nextx][nexty] == 0:
                    temp_lab[nextx][nexty] = 2
                    spread(nextx, nexty, temp_lab)


select_wall(0, 0)
print(answer)