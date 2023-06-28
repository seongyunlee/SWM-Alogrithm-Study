import sys
sys.setrecursionlimit(300000)
input=sys.stdin.readline
N,M=map(int,input().split())
L=[list(map(int,input().split())) for _ in range(N)]
drdc=[[-1,0],[0,1],[0,-1],[1,0]]
cnt=[[-1]*M for _ in range(N)]
def getDFS(r,c):
    if r==N-1 and c==M-1:return 1
    if cnt[r][c]!=-1: return cnt[r][c]
    now_cnt=0
    for dr,dc in drdc:
        if not (0<=r+dr<N and 0<=c+dc<M):continue
        if not L[r+dr][c+dc]<L[r][c]:continue
        now_cnt+=getDFS(r+dr,c+dc)
    cnt[r][c]=now_cnt
    return now_cnt
print(getDFS(0,0))