import sys
input = sys.stdin.readline
R,C,T = map(int,input().split())
M = [list(map(int,input().split())) for _ in range(R)]
A = None 
for i in range(R):
    if M[i][0]==-1:
        A=i
        break
for t in range(T):
    moved = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if M[r][c]==-1:continue
            toward = []
            for dr, dc in [[-1,0],[0,-1],[0,1],[1,0]]:
                if 0<=r+dr<R and 0<=c+dc<C and M[r+dr][c+dc]!=-1:
                    toward.append([r+dr,c+dc])
            for x,y in toward:
                moved[x][y]+=M[r][c]//5
            M[r][c]-=(M[r][c]//5)*len(toward)
    print(*moved,sep="\n",end="\n\n")
    for r in range(R):
        for c in range(C):
            M[r][c]+=moved[r][c]
    print(*M,sep="\n",end="\n\n")
    prev = 0
    for i in range(1,C):
        M[A][i],prev=prev,M[A][i]
    for i in range(A-1,-1,-1):
        M[i][-1],prev=prev,M[i][-1]
    for i in range(C-2,-1,-1):
        M[0][i],prev=prev,M[0][i]
    for i in range(1,A-1):
        M[i][0],prev=prev,M[i][0]
    prev = 0
    for i in range(1,C):
        M[A+1][i],prev=prev,M[A+1][i]
    for i in range(A+2,R):
        M[i][-1],prev=prev,M[i][-1]
    for i in range(C-2,-1,-1):
        M[-1][i],prev=prev,M[-1][i]
    for i in range(R-2,A+1,-1):
        M[i][0],prev=prev,M[i][0]

    print(*M,sep="\n")
print(sum([sum(x) for x in M])+2)