from itertools import combinations
from copy import deepcopy
N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
virus = []
def getSafe(lab,r,c):
    for dr,dc in [[-1,0],[0,-1],[0,1],[1,0]]:
        if not (0<=r+dr<N and 0<=c+dc<M):continue
        if lab[r+dr][c+dc]!=0:continue
        lab[r+dr][c+dc]=2
        getSafe(lab,r+dr,c+dc)
for r in range(N):
    for c in range(M):
        if A[r][c]==2:virus.append([r,c])
answer=0
for newWalls in combinations([(r,c) for r in range(N) for c in range(M) if A[r][c]==0],3):
    nA = deepcopy(A)
    for r,c in newWalls:
        nA[r][c]=1
    for r,c in virus:
        getSafe(nA,r,c)
    answer=max(answer,sum([line.count(0) for line in nA]))
print(answer)
