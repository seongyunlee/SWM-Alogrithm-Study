from heapq import heappop,heappush
N,K = map(int,input().split())
M=list(input())+['-1']
removed=[False]*(N+1)
Q=[]
S=[]
left=[i-1 for i in range(N+1)]
right=[i+1 for i in range(N)]+[-1]
for i in range(N):
    if M[i]<M[i+1]:
        heappush(Q,[i,i+1])
    heappush(S,[M[i],i])
for _ in range(K):
    l,r = None,None
    while True:
        if Q:
            l,r = heappop(Q)
        else:
            _,l=heappop(S)
            r=right[l]
        if removed[r]==False and removed[l]==False:break
    removed[l]=True
    left[r]=left[l]
    if left[l]==-1:continue
    right[left[r]]=r
    if M[r]>M[left[r]]:
        heappush(Q,[left[r],r])
print(''.join([M[i] for i in range(N) if removed[i]==False]))
        
