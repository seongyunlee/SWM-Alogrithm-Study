import sys
import math
input =sys.stdin.readline
N,H = map(int,input().split())
R=[list(map(int,input().split())) for _ in range(N)][::-1]
now=1
ans=-1
A=H+sum([a[1] for a in R if a[0]==2])
for t,a,h in R:
    if t==1:
        now+=a*(math.ceil(h//A)-(1 if h%A==0 else 0))
        ans=now if ans==-1 else max(ans,now)
    else:
        now=max(1,now-h)
        A-=a
print(ans)