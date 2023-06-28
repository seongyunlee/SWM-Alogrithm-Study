import sys
input=sys.stdin.readline
N,M=map(int,input().split())
ID=list(range(N))
S={i:[i] for i in range(N)}
for i in range(M):
    x,y = map(int,input().split())
    if ID[x]==ID[y]:
        print(i+1)
        exit()
    minS,maxS= (ID[x],ID[y]) if len(S[ID[x]])<len(S[ID[y]]) else (ID[y],ID[x])
    for item in S[minS]:
        S[maxS].append(item)
        ID[item]=maxS
    del(S[minS])
print(0)
