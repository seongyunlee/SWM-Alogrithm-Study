import sys
input=sys.stdin.readline
N,M=map(int,input().split())
L=[]
T=None
A=[[-1]*M for _ in range(N)]
for r in range(N):
    L.append(list(map(int,input().split())))
    for c in range(M):
        if L[r][c]==2:T=[r,c]
        elif L[r][c]==0:A[r][c]=0
A[T[0]][T[1]]=0
Q=[T]
cnt=1
while Q:
    nQ=[]
    for r,c in Q:
        for dr,dc in [[-1,0],[0,-1],[0,1],[1,0]]:
            if not (0<=r+dr<N and 0<=c+dc<M): continue            
            if A[r+dr][c+dc]!=-1:
                continue
            A[r+dr][c+dc]=cnt
            nQ.append([r+dr,c+dc])
    Q=nQ
    cnt+=1
for a in A:
    print(*a)
