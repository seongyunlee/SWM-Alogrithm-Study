import sys
input=sys.stdin.readline
N,M = map(int,input().split())
A=[list(map(int,list(input().strip()))) for _ in range(N)]
visit=[[[False,False] for _ in range(M)] for _ in range(N)]
Q=[[0,0,0]]
visit[0][0][0]=True
visit[0][0][1]=True
ans=1
while Q:
    nQ=[]
    for r,c,b in Q:
        if r==N-1 and c==M-1:
            print(ans)
            exit()
        for dr,dc in [[-1,0],[0,-1],[0,1],[1,0]]:
            if not (0<=r+dr<N and 0<=c+dc<M): continue
            if A[r+dr][c+dc]==0 and not visit[r+dr][c+dc][b]:
                visit[r+dr][c+dc][0]=True
                if b==0:visit[r+dr][c+dc][1]=True
                nQ.append([r+dr,c+dc,b])
            if A[r+dr][c+dc]==1 and b==0 and not visit[r+dr][c+dc][b]:
                visit[r+dr][c+dc][1]=True
                nQ.append([r+dr,c+dc,1])
    Q=nQ
    ans+=1
print(-1)