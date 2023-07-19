import sys
input = sys.stdin.readline
N=int(input())
M=[list(map(int,input().split())) for _ in range(N)]
dp=[[[-1,-1,-1] for _ in range(N)] for _ in range(N)]
dir = [[[0,[0,1]],[2,[1,1],[0,1],[1,0]]],[[1,[1,0]],[2,[1,1],[1,0],[0,1]]],[[0,[0,1]],[1,[1,0]],[2,[1,1],[1,0],[0,1]]]]
def getDp(r,c,d):
    if dp[r][c][d]!=-1:return dp[r][c][d]
    if r==N-1 and c==N-1:return 1
    total = 0
    for i in range(len(dir[d])):
        nr,nc=dir[d][i][1]
        if all([0<=r+dr<N and 0<=c+dc<N and M[r+dr][c+dc]==0 for dr,dc in dir[d][i][1:]]):
            total+=getDp(r+nr,c+nc,dir[d][i][0])
    dp[r][c][d]=total
    return total
print(getDp(0,1,0))