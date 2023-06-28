from copy import deepcopy
R,C=map(int,input().split())
M=[list(map(int,input().split())) for _ in range(R)]
cam=[]
for r in range(R):
    for c in range(C):
        if 1<=M[r][c]<6:
            cam.append([M[r][c],r,c])
case=[M]
dir={'l':(0,-1),'r':(0,1),'t':(-1,0),'b':(1,0)}
pos={1:['l','r','t','b'],2:['lr','tb'],3:['tr','tl','bl','br'],4:['lrt','lrb','tbl','tbr'],5:['lrtb']}
for type,r,c in cam:
    new_case=[]
    for cas in case:
        for setCam in pos[type]:
            case_base=deepcopy(cas)
            for direction in setCam:
                dr,dc=dir[direction]
                nowR,nowC=r,c
                while True:
                    nowR+=dr
                    nowC+=dc
                    if not (0<=nowR<R and 0<=nowC<C):break
                    if M[nowR][nowC]==6:break
                    case_base[nowR][nowC]=7
            new_case.append(case_base)
    case=new_case
minShadow=R*C
for c in case:
    minShadow=min(minShadow,sum([line.count(0) for line in c]))   
