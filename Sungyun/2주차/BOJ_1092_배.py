input()
crane=sorted(list(map(int,input().split())))[::-1]
input()
box=sorted(list(map(int,input().split())))[::-1]
box_classfied=[list() for i in range(len(crane))]
a=True
for b in box:
    if b>crane[0]:
        print(-1)
        a=False
        break
    for i in range(len(crane)):
        if (crane[i+1] if not i+1==len(crane) else 0)<b<=crane[i]:
            box_classfied[i].append(b)
            break
s=0
while a:
    #print('s:',s)
    for n_crane in range(len(crane)):
        for n_class in range(n_crane,len(box_classfied)):
            if box_classfied[n_class]:
                box_classfied[n_class].pop()
                #print(box_classfied)
                break
    s=s+1
    if sum([len(i) for i in box_classfied])==0:
        break
if a:print(s)
            
            
                
        
