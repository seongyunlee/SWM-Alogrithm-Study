import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N,L,R = map(int,input().split())
M=[list(map(int,input().split())) for  _ in range(N)]
def openLine():
    line=[[[0,0,0,0] for _ in range(N)] for _ in range(N)]
    move = False
    for r in range(N):
        for c in range(N):
            for dr,dc,dir in [[1,0,0],[0,1,1],[0,-1,2],[-1,0,3]]:
                if not (0<=r+dr<N and 0<=c+dc<N): continue
                if L<=abs(M[r+dr][c+dc]-M[r][c])<=R:
                    line[r][c][dir]=1
                    move= True
    if move==False : return []
    return line
def union(r,c,visit,now,line):
    visit[r][c]=1
    for dr,dc,dir in [[1,0,0],[0,1,1],[0,-1,2],[-1,0,3]]:
        if not (0<=r+dr<N and 0<=c+dc<N): continue
        if visit[r+dr][c+dc]==1:continue
        if line[r][c][dir]==1:
            now.append([r+dr,c+dc])
            union(r+dr,c+dc,visit,now,line)
    return now,visit
day=0
while True:
    line = openLine()
    print(line)
    visit=[[0]*N for _ in range(N)]
    if line==[]:
        print(day)
        break
    for r in range(N):
        for c in range(N):
            print(r,c,visit)
            if visit[r][c]==1:continue
            group,visit = union(r,c,visit,[[r,c]],line)
            if len(group)<2:continue
            print('g',group)
            avg = sum([M[r][c] for r,c in group])//len(group)
            for r,c in group:
                M[r][c]=avg
    day+=1
    print(*M,sep="\n",end="\n\n")

