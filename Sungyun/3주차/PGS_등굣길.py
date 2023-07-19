d=None
import sys
sys.setrecursionlimit(100001)
def dp(r,c):
    if not (0<=r<len(d) and 0<=c<len(d[0])):return 0
    if d[r][c]!=-1:return d[r][c]
    d[r][c]=dp(r,c+1)+dp(r+1,c)
    return d[r][c]
def solution(m, n, puddles):
    global d
    d=[[-1]*m for _ in range(n)]
    d[n-1][m-1]=1
    for x,y in puddles:
        d[y-1][x-1]=0
    return dp(0,0)%1000000007