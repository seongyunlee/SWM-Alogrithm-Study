S,N=map(int,input().split())
x,y=map(int,input().split())
dx=[int(i)*(1 if x>0 else -1) for i in bin(abs(x))[2:].zfill(S)[::-1]]
dy=[int(i)*(1 if y>0 else -1) for i in bin(abs(y))[2:].zfill(S)[::-1]]
N=list(map(int,list(str(N))))
xx=[2,1,4,3]
yy=[4,3,2,1]
for move,pos,up in [(dx,xx,[1,4]),(dy,yy,[1,2])]:
    carry=0
    for i,d in enumerate(move):
        d+=int(carry)
        idx=i+1
        carry=int((abs(d)==2) or (N[-idx] in up and d>0) or (N[-idx] not in up and d<0))*(1 if d>0 else -1)
        if abs(d)==1:N[-idx]=pos[N[-idx]-1]
        if idx==S and carry:
            print(-1)
            exit()
print(''.join([str(i) for i in N]))

