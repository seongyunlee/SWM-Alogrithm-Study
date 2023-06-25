import math
input()
crane=sorted(list(map(int,input().split())))
input()
box=sorted(list(map(int,input().split())))
cnt=[0]*len(crane)
b=0
for i in range(len(crane)):
    movable=0
    for j in range(b,len(box)):
        if crane[i]<box[j]:
            b=j
            break
        if j==len(box)-1:b=len(box)
        movable+=1
    cnt[i]=movable
print(crane,box,cnt)
remain=len(box)
ans=0
for i in range(len(cnt)):
    amt=len(crane)-i
    time=math.ceil(cnt[i]/amt)
    if amt*time>remain: time=math.ceil(remain/amt)
    ans+=time
    remain-=amt*time
    print('t',time,remain)
    if remain<=0:
        print(ans)
        break
if remain>0:
    print(-1)