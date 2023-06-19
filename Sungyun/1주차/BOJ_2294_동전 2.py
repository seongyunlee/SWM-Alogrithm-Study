import sys
input= sys.stdin.readline
N,K=map(int,input().split())
C=[int(input()) for _ in range(N)]
C.sort()
dp=[[p//C[0] if p%C[0]==0 else 1000001 for p in range(K+1)]]+[[1000001]*(K+1) for _ in range(N)]
print(dp)
for i in range(1,len(dp)):
    for j in range(len(dp[0])):
        dp[i][j]=min([dp[i-1][j-C[i]*p] for p in range(j//C[i]+1)])
print(dp)
if dp[K][N-1]>=1000001:
    print(-1)
else: print(dp[K][N-1])