import sys
from itertools import combinations
# 0 = 빈칸, 1 = 집, 2 = 치킨집, 치킨거리 = 치킨집과의 거리, 도시의 치킨거리 = 모든 집의 치킨거리의 합
N, M = map(int, sys.stdin.readline().split())
city = []
chicken = []
house = []
answer = 9801

for i in range(N):
    city.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

num = [i for i in range(len(chicken))]
out = list(combinations(num, M))

for store in out:
    tempans = 0
    for i in range(len(house)):
        temp = 100
        for j in store:
            tempdis = abs(house[i][0] - chicken[j][0]) + abs(house[i][1] - chicken[j][1])

            if tempdis < temp:
                temp = tempdis

        tempans += temp
    if tempans < answer:
        answer = tempans

print(answer)
