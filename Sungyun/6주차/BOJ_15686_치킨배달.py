import sys
from itertools import combinations
input = sys.stdin.readline
N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
H=[]
C=[]
for r in range(N):
    for c in range(N):
        if A[r][c] == 1:
            H.append([r,c])
        elif A[r][c]==2:
            C.append([r,c])
def getChickDis(home,chicklist):
    hr,hc = home
    return min([abs(cr-hr)+abs(cc-hc) for cr,cc in chicklist])
minC = 2*N*N*N
for combi in combinations(C,M):
    minC= min(minC,sum([getChickDis(home,combi) for home in H]))
print(minC)
    
